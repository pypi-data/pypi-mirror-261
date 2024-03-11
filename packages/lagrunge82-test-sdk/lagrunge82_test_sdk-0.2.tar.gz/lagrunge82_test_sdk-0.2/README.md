# `ApiClient` Class Description

## Installation:
```pip install lagrunge82-test-sdk```

## Features:

* Retrieve weather information for specified cities.
* Support for two operation modes: "on-demand" and "polling".

## Operation Modes:

* "On-demand":
    * The SDK updates weather information only upon user request.
    * Suitable for applications where weather information is not critical and does not require instant updates.
* "Polling":
    * The SDK periodically requests new weather information for all stored locations to have zero latency response to user requests.
    * Suitable for applications where quick access to up-to-date weather information is required.


## Usage:

```Python
from openweather_sdk.api_client import ApiClient

# Create an API client instance with your API key
api_client = ApiClient("YOUR_API_KEY", mode='on-demand')

# Get weather data for a city
weather_data = api_client.get_weather("London")

# Access weather information
print(f"Temperature: {weather_data['main']['temp']}")
```

## Additional Features:
* **Data caching:**
    * The SDK caches received weather data to reduce the number of API requests.
    * The default Time-to-Live (TTL) is 600 seconds (10 minutes).
    * You can change the TTL if needed.

* **Geocoding:**
    * The SDK determines geographic coordinates by city name.

* **Error handling:**
    * The SDK handles errors that occur when interacting with the API.
    * You can get error information and handle it according to your requirements.

```Python
# Get weather data for 5 cities
cities = ["London", "Paris", "Berlin", "New York", "Tokyo"]

for city in cities:
    try:
        weather_data = api_client.get_weather(city)
        print(f"Weather data for {city}:")
        print(weather_data)
    except APIException as e:
        print(f"Error getting weather data for {city}:")
        print(e.message)
```

### Other features:
* **Multithreading:**
    * The SDK can perform requests to the OpenWeatherMap API in multithreaded mode, which can improve performance.