from datetime import date


class Book:
    """Represent a printed book."""

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

    def get_age(self):
        """Return the number of years since publication."""
        return date.today().year - self.year


class EBook(Book):
    """Represent an electronic book with a file size in megabytes."""

    def __init__(self, title, author, year, file_size):
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        return (
            f"Title: {self.title}, Author: {self.author}, Year: {self.year}, "
            f"File Size: {self.file_size} MB"
        )
