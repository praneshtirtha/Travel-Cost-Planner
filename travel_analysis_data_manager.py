"""Ananto Shariar 
Contributions:
- Travel-option comparison
- Cost-per-person calculation
- Recommendation logic
- CSV save/load
- File-error handling
"""

import csv
import os

from input_validation_transport_manager import calculate_transport_cost

# This list defines the exact column order used when plans are written to CSV.
# Using one shared field list keeps saving and loading consistent.
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
   # It will return the estimated cost for one traveller and travellers is a valid integer so it can not be divided by zero
     
    return final_cost / travellers


def save_plan(option_data, filename):
    try:

       # It is wroking as copy so that the value does not change the working dictionary.
        option_data = dict(option_data)

        """ Check it again before saving transport cost """
        option_data["transport_cost"] = calculate_transport_cost(
            option_data["transport_cost"]
        )

        # A header will use only when the file is new or empty 
        file_exists = os.path.exists(filename)
        file_is_empty = (not file_exists) or os.path.getsize(filename) == 0

        # Append mode keeps all the traval plan that are already in the csv file
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=CSV_FIELDS)
            if file_is_empty:
                writer.writeheader()
            writer.writerow(option_data)

        print("Travel plan saved successfully.")
        return True

    except (OSError, ValueError, KeyError, TypeError, csv.Error) as error:
        print(f"File error: the travel plan could not be saved ({error}).")
        return False


def load_plans(filename):
   
    #Load valid traval plans from CSV and row will become one dictionary in this list.
    travel_options = []
    # If there is no previous saved file it will be a missing file. 
    if not os.path.exists(filename):
        return travel_options

    try:
       # An empty file do not have header or plan records.
        if os.path.getsize(filename) == 0:
            return travel_options

        with open(filename, "r", newline="", encoding="utf-8") as file:
           
            reader = csv.DictReader(file)

            if reader.fieldnames is None:
                return travel_options

            # Data begins on row 2 because row 1 contains the column headings.
            for row_number, row in enumerate(reader, start=2):
                try:
                    # CSV values are text, so numeric fields must be converted back in intger or float.
                    
                    option = {
                        "option_name": row["option_name"],
                        "destination": row["destination"],
                        "travellers": int(row["travellers"]),
                        "transport_type": row["transport_type"],
                        "transport_cost": calculate_transport_cost(row["transport_cost"]),
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

                    # Store the completed plan dictionary in the in-memory list.
                    travel_options.append(option)

               
                   # If one row skipped
                except (ValueError, KeyError, TypeError):
                    print(
                        f"Warning: invalid stored data on CSV row {row_number} was skipped."
                    )

    # If there is a permission problems it will reported without terminating the app.
    except OSError as error:
        print(f"File error: saved travel plans could not be read ({error}).")

    return travel_options


def compare_options(option_list):
    
    # The comparison rules require two plans.
    if len(option_list) < 2:
        raise ValueError("At least two travel options are required.")

    # The first two dictionaries are the plans which was selected by the user.
    option1 = option_list[0]
    option2 = option_list[1]

    # Find the absolute price difference so the result is never negative.
    cost1 = option1["final_cost"]
    cost2 = option2["final_cost"]
    cost_difference = abs(cost1 - cost2)

    # Record the cheaper plan separately for display purposes.
    if cost1 < cost2:
        cheaper = option1
    elif cost2 < cost1:
        cheaper = option2
    else:
        cheaper = None

    # "Near Budget" and "Within Budget" both count as fitting the budget.
    option1_fits = option1["budget_status"] != "Over Budget"
    option2_fits = option2["budget_status"] != "Over Budget"

    # First priority is recommend the only option that fits its budget.
    if option1_fits and not option2_fits:
        recommended = option1
        reason = "It fits the budget while the other option is over budget."

    elif option2_fits and not option1_fits:
        recommended = option2
        reason = "It fits the budget while the other option is over budget."

    else:
        # When both plans have the same budget outcome, determine whether their prices are close. "Close" means within 5% of the cheaper plan's cost.

        lower_cost = min(cost1, cost2)
        five_percent_limit = lower_cost * 0.05

        if cost_difference <= five_percent_limit:
            # When prices are close, comfort becomes the next priority.
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
                    # Travel time is the final tie-breaker when cost and comfort are exactly equal.
                
                    if option1["travel_time"] <= option2["travel_time"]:
                        recommended = option1
                    else:
                        recommended = option2
                    reason = "Cost and comfort are equal, so shorter travel time was preferred."
        else:
            # If the prices are not close, the less expensive plan is preferred.
            if cost1 <= cost2:
                recommended = option1
            else:
                recommended = option2
            reason = "The lower-cost option was preferred."

    # A result dictionary makes every comparison output easy to identify and use.
    return {
        "cheaper": cheaper,
        "cost_difference": cost_difference,
        "recommended": recommended,
        "reason": reason,
    }
