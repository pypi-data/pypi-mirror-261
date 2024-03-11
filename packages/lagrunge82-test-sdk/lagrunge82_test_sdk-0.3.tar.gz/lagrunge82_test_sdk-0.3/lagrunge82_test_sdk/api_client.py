import json
import time
import requests
import threading

from typing import Literal, Dict
from urllib.parse import urlencode, urlunparse

from lagrunge82_test_sdk.components.models import CityGeo, CityData, CityWeather
from lagrunge82_test_sdk.exceptions import (ConnectionException, APIException)


class ApiClient:
    """
    The `ApiClient` class is designed to interact with the OpenWeatherMap API,
    providing weather data for specified cities.

    It's possible to create only one instance of the `ApiClient` class per API key.

    It supports two modes of operation: "on-demand" and "polling."
    *  **On-demand mode:** The SDK updates the weather information only on customer requests.
    *  **Polling mode:** The SDK requests new weather information for all stored locations
        at regular intervals to have zero-latency response for customer requests.


    Attributes:
        _instances (dict): A dictionary to store instances of the `ApiClient` class
                    with their respective API keys.
        _ttl (int): Time-to-live (in seconds) for cached weather data.
        _hostname (str): The API hostname for OpenWeatherMap.
        _mode (str): The operating mode, either "on-demand" or "polling".
    """
    _instances = {}
    _ttl = 600
    _hostname = 'api.openweathermap.org'
    _mode = None

    def __new__(cls, api_key: str, *args, **kwargs):
        if api_key not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[api_key] = instance
            return instance
        return cls._instances[api_key]

    def __init__(self, api_key: str, mode: Literal['on-demand', 'polling'] = None):
        self._cities = {}
        self._api_key = api_key
        self._thread = threading.Thread(target=self._poller)
        self._stop_polling = threading.Event()
        if self._mode is None:
            self._mode = 'on-demand' if mode is None else mode
        else:
            if mode is not None and self._mode != mode:
                raise ValueError(
                    f'The {self.__class__.__name__} instance with the API key `{api_key}` '
                    f'has already been initialized in `{self._mode}` mode'
                )
        if mode == 'polling':
            self._thread.start()

    def _poller(self):
        """
        Polls OpenWeatherMap for weather data for cities stored in `_cities` at regular intervals
        when in "polling" mode.

        """
        while not self._stop_polling.is_set():
            for city, data in self._cities.items():
                if time.time() - data.updated_at >= self._ttl - 20:
                    query = {'lat': data.geo.lat, 'lon': data.geo.lon, 'appid': self._api_key}
                    url = self._get_url('/data/2.5/weather', query)
                    weather = CityWeather(**self.__request(url))
                    data.weather = weather
                    data.updated_at = time.time()
            time.sleep(10)

    @staticmethod
    def __request(url) -> Dict:
        """

        Perform a GET request to the specified URL, handles errors and returns the JSON response.
        :param url: The URL to send the GET request.
        :type url: str
        :return: A dictionary representing the JSON response from the server.
        :rtype: Dict
        """
        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            raise ConnectionException(e)
        if response.status_code == 200:
            return response.json()
        raise APIException(response.json())

    def _add_city(self, city: str, data: CityData):
        """
        Add city data to the internal city storage.
        If the number of stored cities exceeds the maximum limit (10),
        the oldest city is removed before adding the new one.

        :param city:The name of the city to add.
        :type city: str
        :param data: An instance of :class:`CityData` containing information about the city.
        :type data: :class:`CityData`
        """
        if len(self._cities) == 10:
            redundant_city = next(iter(self._cities.keys()))
            self._cities.pop(redundant_city)
        self._cities[city] = data

    def get_weather(self, city: str) -> Dict:
        """
        Retrieve weather data for the specified city.
        If the data is available in the cache and not expired, it is returned;
        otherwise, a new request is made to the OpenWeatherMap API.

        :param city:The name of the city for which weather data is requested.
        :type city: str

        :return: A dictionary representing the weather data for the specified city.
        :rtype: Dict
        """
        if city in self._cities:
            if time.time() - self._cities[city].updated_at < self._ttl:
                return self._cities[city].weather.model_dump()
            geo = self._cities[city].geo
        else:
            geo = CityGeo(**self._geocoder(city)[0])
        query = {'lat': geo.lat, 'lon': geo.lon, 'appid': self._api_key}
        url = self._get_url('/data/2.5/weather', query)
        weather = CityWeather(**self.__request(url))
        data = CityData(geo=geo, weather=weather, updated_at=time.time())
        self._add_city(city, data)
        return weather.model_dump()

    def _geocoder(self, city):
        """
        Retrieve geographical data for a given city using the OpenWeatherMap geocoding API.

        :param city: The name of the city for which geographical data is requested.
        :type city: str

        :return: A dictionary containing geographical information for the specified city.
        :rtype: Dict
        """
        query = {'q': city, 'appid': self._api_key}
        url = self._get_url('/geo/1.0/direct', query)
        return self.__request(url)

    def _get_url(self, path: str, query: Dict):
        """
        Construct and return a URL using the specified path and query parameters.

        :param path:The path component of the URL.
        :type path: str
        :param query: A dictionary containing query parameters to be included in the URL.
        :type query: Dict

        :return: A fully-formed URL incorporating the specified path and query parameters.
        :rtype: str

        .. note::
           The method does not validate the components of the URL or check for the existence
           of the hostname.
        """
        return urlunparse(('https', self._hostname, path, '', urlencode(query), ''))

    def unload(self):
        """
        Unloads the resources associated with the current API key.

        :return:
        """
        if self._mode == 'polling':
            # stop poller working in another thread
            self._stop_polling.set()
            self._thread.join()

        # Remove the instance associated with the current API key
        del self._instances[self._api_key]




