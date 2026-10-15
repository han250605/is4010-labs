import requests


class WeatherAPI:
    """Fetch current and forecast weather data from WeatherAPI."""

    def __init__(self, api_key, base_url="https://api.weatherapi.com/v1"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def _request_json(self, endpoint, location, **extra_params):
        params = {"key": self.api_key, "q": location}
        params.update(extra_params)

        try:
            response = requests.get(
                f"{self.base_url}/{endpoint}",
                params=params,
                timeout=10,
            )
            response.raise_for_status()
            return response.json()
        except (requests.exceptions.RequestException, ValueError, TypeError):
            return None

    def get_current_weather(self, location):
        return self._request_json("current.json", location)

    def get_forecast(self, location, days=3):
        if not 1 <= days <= 3:
            raise ValueError("days must be between 1 and 3")
        return self._request_json("forecast.json", location, days=days)


def format_current_weather(data):
    """Format the current-weather payload as CITY, COUNTRY: TEMP°F, CONDITION."""
    location = data["location"]
    current = data["current"]
    return (
        f"{location['name']}, {location['country']}: "
        f"{current['temp_f']}°F, {current['condition']['text']}"
    )


def format_forecast(data):
    """Format the first forecast day as DATE: high TEMP°F, low TEMP°F, CONDITION."""
    forecast_day = data["forecast"]["forecastday"][0]
    day = forecast_day["day"]
    return (
        f"{forecast_day['date']}: high {day['maxtemp_f']}°F, "
        f"low {day['mintemp_f']}°F, {day['condition']['text']}"
    )
