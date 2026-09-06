"""Ananto Shariar | 2211431042
Responsibilities from the planning document:
- Travel-option comparison
- Cost-per-person calculation
- Recommendation logic
- CSV save/load
- File-error handling
"""

import csv
import os

CSV_FIELDS = [
    "option_name",
    "destination",
    "travellers",
    "transport_type",
    "transport_cost",
    "nights",
    "rooms_required",
    "accommodation_cost",
    "food_cost",
    "activity_cost",
    "other_cost",
    "subtotal",
    "discount",
    "final_cost",
    "cost_per_person",
    "budget",
    "budget_status",
    "comfort_rating",
    "travel_time",
]


def calculate_cost_per_person(final_cost, travellers):
    """Return the estimated cost for one traveller."""
    return final_cost / travellers


def save_plan(option_data, filename):
    """Append one travel plan to the CSV file."""
    file_exists = os.path.exists(filename)
    file_is_empty = (not file_exists) or os.path.getsize(filename) == 0

    try:
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
            if file_is_empty:
                writer.writeheader()
            writer.writerow(option_data)
        print("Travel plan saved successfully.")
        return True
    except OSError as error:
        print(f"File error: the travel plan could not be saved ({error}).")
        return False


def load_plans(filename):
    """Load valid travel plans from CSV and safely skip malformed rows."""
    travel_options = []

    if not os.path.exists(filename):
        return travel_options

    try:
        if os.path.getsize(filename) == 0:
            return travel_options

        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                return travel_options

            for row_number, row in enumerate(reader, start=2):
                try:
                    option = {
                        "option_name": row["option_name"],
                        "destination": row["destination"],
                        "travellers": int(row["travellers"]),
                        "transport_type": row["transport_type"],
                        "transport_cost": float(row["transport_cost"]),
                        "nights": int(row["nights"]),
                        "rooms_required": int(row["rooms_required"]),
                        "accommodation_cost": float(row["accommodation_cost"]),
                        "food_cost": float(row["food_cost"]),
                        "activity_cost": float(row["activity_cost"]),
                        "other_cost": float(row["other_cost"]),
                        "subtotal": float(row["subtotal"]),
                        "discount": float(row["discount"]),
                        "final_cost": float(row["final_cost"]),
                        "cost_per_person": float(row["cost_per_person"]),
                        "budget": float(row["budget"]),
                        "budget_status": row["budget_status"],
                        "comfort_rating": int(row["comfort_rating"]),
                        "travel_time": float(row["travel_time"]),
                    }
                    travel_options.append(option)
                except (ValueError, KeyError, TypeError):
                    print(
                        f"Warning: invalid stored data on CSV row {row_number} was skipped."
                    )

    except OSError as error:
        print(f"File error: saved travel plans could not be read ({error}).")

    return travel_options


def compare_options(option_list):
    """Compare two travel options and return a recommendation summary."""
    if len(option_list) < 2:
        raise ValueError("At least two travel options are required.")

    option1 = option_list[0]
    option2 = option_list[1]

    cost1 = option1["final_cost"]
    cost2 = option2["final_cost"]
    cost_difference = abs(cost1 - cost2)

    if cost1 < cost2:
        cheaper = option1
    elif cost2 < cost1:
        cheaper = option2
    else:
        cheaper = None

    option1_fits = option1["budget_status"] != "Over Budget"
    option2_fits = option2["budget_status"] != "Over Budget"

    if option1_fits and not option2_fits:
        recommended = option1
        reason = "It fits the budget while the other option is over budget."

    elif option2_fits and not option1_fits:
        recommended = option2
        reason = "It fits the budget while the other option is over budget."

    else:
        lower_cost = min(cost1, cost2)
        five_percent_limit = lower_cost * 0.05

        if cost_difference <= five_percent_limit:
            comfort1 = option1["comfort_rating"]
            comfort2 = option2["comfort_rating"]

            if comfort1 > comfort2:
                recommended = option1
                reason = "The costs are close, so the higher comfort rating was preferred."
            elif comfort2 > comfort1:
                recommended = option2
                reason = "The costs are close, so the higher comfort rating was preferred."
            else:
                if cost1 < cost2:
                    recommended = option1
                    reason = "Comfort is equal, so the lower-cost option was preferred."
                elif cost2 < cost1:
                    recommended = option2
                    reason = "Comfort is equal, so the lower-cost option was preferred."
                else:
                    if option1["travel_time"] <= option2["travel_time"]:
                        recommended = option1
                    else:
                        recommended = option2
                    reason = "Cost and comfort are equal, so shorter travel time was preferred."
        else:
            if cost1 <= cost2:
                recommended = option1
            else:
                recommended = option2
            reason = "The lower-cost option was preferred."

    return {
        "cheaper": cheaper,
        "cost_difference": cost_difference,
        "recommended": recommended,
        "reason": reason,
    }
