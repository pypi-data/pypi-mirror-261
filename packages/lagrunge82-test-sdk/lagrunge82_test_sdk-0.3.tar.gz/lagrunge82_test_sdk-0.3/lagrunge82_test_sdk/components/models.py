from __future__ import annotations
from pydantic import BaseModel, Field, field_validator


class CityData(BaseModel):
    geo: CityGeo
    weather: CityWeather = None
    updated_at: float = None


class CityGeo(BaseModel):
    name: str
    lat: float
    lon: float
    country: str
    state: str


class CityWeather(BaseModel):
    weather: Weather
    temperature: Temperature = Field(alias='main')
    visibility: int
    wind: Wind
    datetime: int = Field(alias='dt')
    sys: Sys
    timezone: int
    name: str

    @field_validator('weather', mode='before')
    def weather_validation(cls, value):
        return value[0]


class Weather(BaseModel):
    main: str
    description: str


class Temperature(BaseModel):
    temp: float
    feels_like: float


class Wind(BaseModel):
    speed: float


class Sys(BaseModel):
    sunrise: int
    sunset: int
