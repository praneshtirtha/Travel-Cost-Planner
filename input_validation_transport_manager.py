"""Md. Nasim Taif 
Contributions:
- Main menu support
- Travel-option input
- Input validation
- Transport-cost calculation
- main.py integration support
"""


import math


def get_non_empty_text(prompt):
    """Return a non-empty text value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Input cannot be empty. Please try again.")


def get_positive_integer(prompt):
    """Return a whole number greater than 0."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Please enter a whole number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def get_non_negative_integer(prompt):
    """Return a whole number that is 0 or greater."""
    while True:
        try:
            value = int(input(prompt))
            if value >= 0:
                return value
            print("Please enter 0 or a positive whole number.")
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def get_non_negative_float(prompt):
    """Return a numeric value that is 0 or greater."""
    while True:
        try:
            value = float(input(prompt))
            if math.isfinite(value) and value >= 0:
                return value
            print("Please enter a finite number that is 0 or greater.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_positive_float(prompt):
    """Return a numeric value greater than 0."""
    while True:
        try:
            value = float(input(prompt))
            if math.isfinite(value) and value > 0:
                return value
            print("Please enter a finite number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_comfort_rating():
    """Return a comfort rating from 1 to 5."""
    while True:
        try:
            rating = int(input("Comfort rating (1-5): "))
            if 1 <= rating <= 5:
                return rating
            print("Comfort rating must be between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a whole number from 1 to 5.")


def calculate_transport_cost(transport_cost):
    """Validate and return the entered total transport expense for the group."""
    transport_cost = float(transport_cost)
    if not math.isfinite(transport_cost) or transport_cost < 0:
        raise ValueError("Transport cost must be a finite number that is 0 or greater.")
    return transport_cost
