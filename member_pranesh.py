"""Pranesh Majumder Tirtha | 2222899042
Responsibilities from the planning document:
- Accommodation and room calculation
- Food and activity cost calculation
- Discount logic
- Budget checking
"""

import math


def calculate_accommodation_cost(travellers, capacity, room_cost, nights):
    """Return rooms required and total accommodation cost."""
    rooms_required = math.ceil(travellers / capacity)
    accommodation_total = rooms_required * room_cost * nights
    return rooms_required, accommodation_total


def calculate_food_cost(travellers, days, food_rate):
    """Calculate total food expense."""
    return travellers * days * food_rate


def calculate_activity_cost(travellers, activity_rate):
    """Calculate total activity expense."""
    return travellers * activity_rate


def calculate_subtotal(costs):
    """Add all cost categories stored in a dictionary."""
    return sum(costs.values())


def apply_travel_discount(subtotal, travellers):
    """Apply a 10% discount when there are 5 or more travellers."""
    if travellers >= 5:
        discount = subtotal * 0.10
    else:
        discount = 0.0

    final_cost = subtotal - discount
    return discount, final_cost


def check_budget(final_cost, budget):
    """Return budget status and the difference from the available budget."""
    ratio = final_cost / budget

    if final_cost > budget:
        status = "Over Budget"
    elif ratio >= 0.90:
        status = "Near Budget"
    else:
        status = "Within Budget"

    difference = budget - final_cost
    return status, difference
