import json
import os


class FavoritesManager:
    """Manage favorite place names and their locations."""

    def __init__(self, filename):
        self.filename = filename
        directory = os.path.dirname(filename)
        if directory:
            os.makedirs(directory, exist_ok=True)
        self._favorites = self._load()

    def _load(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError, OSError):
            return {}

        if isinstance(data, dict):
            return {str(key).lower(): str(value) for key, value in data.items()}
        return {}

    def _save(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self._favorites, file, indent=4)

    def add(self, name, location):
        key = name.strip().lower()
        if key in self._favorites:
            return False
        self._favorites[key] = location
        self._save()
        return True

    def remove(self, name):
        key = name.strip().lower()
        if key not in self._favorites:
            return False
        del self._favorites[key]
        self._save()
        return True

    def list_all(self):
        return dict(self._favorites)

    def get_location(self, name):
        return self._favorites.get(name.strip().lower())
