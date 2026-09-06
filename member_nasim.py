"""Md. Nasim Taif 
ID: 2212601042
Responsibilities from the planning document:
- Main menu support
- Travel-option input
- Input validation
- Transport-cost calculation
- main.py integration support
"""


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
            if value >= 0:
                return value
            print("The value cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_positive_float(prompt):
    """Return a numeric value greater than 0."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than 0.")
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


def calculate_transport_cost(fixed_cost, per_person, travellers):
    """Calculate the total transport expense."""
    return fixed_cost + (per_person * travellers)
