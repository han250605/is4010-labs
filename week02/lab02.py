"""Implementations for Lab 02."""


def make_greeting(name: str) -> str:
    """Return a greeting using the supplied name."""
    return f"Hello, {name}!"


def is_even(number: int) -> bool:
    """Return True when number is even and False otherwise."""
    return number % 2 == 0


def count_vowels(text: str) -> int:
    """Count a, e, i, o, and u without regard to case."""
    return sum(character.lower() in "aeiou" for character in text)
