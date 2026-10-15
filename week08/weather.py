import argparse
import os
import sys

from week08.favorites import FavoritesManager
from week08.weather_api import WeatherAPI, format_current_weather, format_forecast

FAVORITES_FILE = os.path.join(os.path.dirname(__file__), "favorites.json")


def load_api_key():
    """Load the WeatherAPI key from the environment or local config file."""
    key = os.getenv("WEATHER_API_KEY")
    if key:
        return key

    try:
        from week08 import config  # type: ignore

        if hasattr(config, "WEATHER_API_KEY"):
            return config.WEATHER_API_KEY
    except Exception:
        return None

    return None


def build_parser():
    parser = argparse.ArgumentParser(description="Weather CLI")
    subparsers = parser.add_subparsers(dest="command")

    current_parser = subparsers.add_parser("current", help="Get current weather")
    current_parser.add_argument("location")

    forecast_parser = subparsers.add_parser("forecast", help="Get a forecast")
    forecast_parser.add_argument("location")
    forecast_parser.add_argument("--days", type=int, default=3)

    favorites_parser = subparsers.add_parser("favorites", help="Manage favorites")
    favorites_subparsers = favorites_parser.add_subparsers(dest="favorites_command")

    add_parser = favorites_subparsers.add_parser("add", help="Add a favorite")
    add_parser.add_argument("name")
    add_parser.add_argument("location")

    list_parser = favorites_subparsers.add_parser("list", help="List favorites")
    list_parser  # keeps the parser in scope for tests

    remove_parser = favorites_subparsers.add_parser("remove", help="Remove a favorite")
    remove_parser.add_argument("name")

    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 1

    api_key = load_api_key()
    if not api_key:
        print("API key is missing. Set WEATHER_API_KEY or update config.py.", file=sys.stderr)
        return 1

    client = WeatherAPI(api_key)
    manager = FavoritesManager(FAVORITES_FILE)

    if args.command == "current":
        location = manager.get_location(args.location) or args.location
        weather_data = client.get_current_weather(location)
        if weather_data is None:
            print(f"Unable to fetch weather for {location}", file=sys.stderr)
            return 1
        print(format_current_weather(weather_data))
        return 0

    if args.command == "forecast":
        location = manager.get_location(args.location) or args.location
        try:
            weather_data = client.get_forecast(location, days=args.days)
        except ValueError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        if weather_data is None:
            print(f"Unable to fetch forecast for {location}", file=sys.stderr)
            return 1
        print(format_forecast(weather_data))
        return 0

    if args.command == "favorites":
        if args.favorites_command == "add":
            if manager.get_location(args.name) is not None:
                print(f"Favorite '{args.name}' already exists.", file=sys.stderr)
                return 1
            manager.add(args.name, args.location)
            return 0

        if args.favorites_command == "list":
            for name, location in manager.list_all().items():
                print(f"{name}: {location}")
            return 0

        if args.favorites_command == "remove":
            if not manager.remove(args.name):
                print(f"Favorite '{args.name}' not found.", file=sys.stderr)
                return 1
            return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
