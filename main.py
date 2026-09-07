"""Travel Cost Planner and Option Comparator
CSE101 - Section 2 - Group 04

main.py integration responsibility: Md. Nasim Taif
The program imports group-member functions through travel_utils.py.
"""

from travel_utils import (
    calculate_transport_cost,
    get_non_empty_text,
    get_positive_integer,
    get_non_negative_integer,
    get_non_negative_float,
    get_positive_float,
    get_comfort_rating,
    calculate_accommodation_cost,
    calculate_food_cost,
    calculate_activity_cost,
    calculate_subtotal,
    apply_travel_discount,
    check_budget,
    calculate_cost_per_person,
    compare_options,
    save_plan,
    load_plans,
)

FILE_NAME = "travel_plans.csv"

def display_plan(plan, number=None):
    print("\n" + "=" * 60)

    if number is not None:
        print(f"TRAVEL OPTION {number}")
        print("-" * 60)

    print(f"Option Name          : {plan['option_name']}")
    print(f"Destination          : {plan['destination']}")
    print(f"Travellers           : {plan['travellers']}")
    print(f"Transport Type       : {plan['transport_type']}")
    print(f"Transport Cost       : Tk. {plan['transport_cost']:.2f}")
    print(f"Nights               : {plan['nights']}")
    print(f"Rooms Required       : {plan['rooms_required']}")
    print(f"Accommodation Cost   : Tk. {plan['accommodation_cost']:.2f}")
    print(f"Food Cost            : Tk. {plan['food_cost']:.2f}")
    print(f"Activity Cost        : Tk. {plan['activity_cost']:.2f}")
    print(f"Other Cost           : Tk. {plan['other_cost']:.2f}")
    print("-" * 60)
    print(f"Subtotal             : Tk. {plan['subtotal']:.2f}")
    print(f"Discount             : Tk. {plan['discount']:.2f}")
    print(f"Final Estimated Cost : Tk. {plan['final_cost']:.2f}")
    print(f"Cost Per Person      : Tk. {plan['cost_per_person']:.2f}")
    print(f"Budget               : Tk. {plan['budget']:.2f}")
    print(f"Budget Status        : {plan['budget_status']}")
    print(f"Comfort Rating       : {plan['comfort_rating']}/5")
    print(f"Travel Time          : {plan['travel_time']:.2f} hours")
    print("=" * 60)


def display_budget_difference(difference):
    if difference > 0:
        print(f"Amount under budget: Tk. {difference:.2f}")
    elif difference < 0:
        print(f"Amount over budget : Tk. {abs(difference):.2f}")
    else:
        print("The final cost exactly matches the budget.")


def view_saved_options(travel_options):
    if not travel_options:
        print("\nNo saved travel plans found.")
        return

    print("\nSAVED TRAVEL OPTIONS")
    for index, plan in enumerate(travel_options, start=1):
        display_plan(plan, index)


def create_travel_option():
    print("\n" + "=" * 60)
    print("CREATE TRAVEL OPTION")
    print("=" * 60)

    option_name = get_non_empty_text("Option name: ")
    destination = get_non_empty_text("Destination: ")
    travellers = get_positive_integer("Number of travellers: ")
    transport_type = get_non_empty_text("Transport type: ")

    fixed_transport_cost = get_non_negative_float(
        "Fixed transport cost (Tk.): "
    )
    transport_cost_per_person = get_non_negative_float(
        "Transport cost per person (Tk.): "
    )

    nights = get_non_negative_integer("Number of nights: ")
    room_capacity = get_positive_integer("Room capacity: ")
    room_cost_per_night = get_non_negative_float(
        "Room cost per night (Tk.): "
    )
    food_rate = get_non_negative_float(
        "Food cost per person per day (Tk.): "
    )
    activity_rate = get_non_negative_float(
        "Activity cost per person (Tk.): "
    )
    other_cost = get_non_negative_float("Other fixed cost (Tk.): ")
    budget = get_positive_float("Available budget (Tk.): ")
    comfort_rating = get_comfort_rating()
    travel_time = get_positive_float("Estimated travel time (hours): ")

    transport_cost = calculate_transport_cost(
        fixed_transport_cost,
        transport_cost_per_person,
        travellers,
    )

    rooms_required, accommodation_cost = calculate_accommodation_cost(
        travellers,
        room_capacity,
        room_cost_per_night,
        nights,
    )

    travel_days = nights + 1
    food_cost = calculate_food_cost(travellers, travel_days, food_rate)
    activity_cost = calculate_activity_cost(travellers, activity_rate)

    costs = {
        "transport": transport_cost,
        "accommodation": accommodation_cost,
        "food": food_cost,
        "activity": activity_cost,
        "other": other_cost,
    }

    subtotal = calculate_subtotal(costs)
    discount, final_cost = apply_travel_discount(subtotal, travellers)
    cost_per_person = calculate_cost_per_person(final_cost, travellers)
    budget_status, budget_difference = check_budget(final_cost, budget)

    option = {
        "option_name": option_name,
        "destination": destination,
        "travellers": travellers,
        "transport_type": transport_type,
        "transport_cost": transport_cost,
        "nights": nights,
        "rooms_required": rooms_required,
        "accommodation_cost": accommodation_cost,
        "food_cost": food_cost,
        "activity_cost": activity_cost,
        "other_cost": other_cost,
        "subtotal": subtotal,
        "discount": discount,
        "final_cost": final_cost,
        "cost_per_person": cost_per_person,
        "budget": budget,
        "budget_status": budget_status,
        "comfort_rating": comfort_rating,
        "travel_time": travel_time,
    }

    display_plan(option)
    display_budget_difference(budget_difference)
    print("Note: This is an Estimated Travel Cost; actual prices may vary.")

    if save_plan(option, FILE_NAME):
        return option

    return None


def choose_saved_option(travel_options, prompt):
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= len(travel_options):
                return choice - 1
            print(f"Please enter a number from 1 to {len(travel_options)}.")
        except ValueError:
            print("Invalid input. Please enter a valid option number.")


def compare_saved_options(travel_options):
    if len(travel_options) < 2:
        print("\nAt least two travel options are required for comparison.")
        return

    print("\nAVAILABLE OPTIONS")
    for index, option in enumerate(travel_options, start=1):
        print(
            f"{index}. {option['option_name']} | "
            f"Tk. {option['final_cost']:.2f} | {option['budget_status']}"
        )

    first_index = choose_saved_option(travel_options, "Select first option: ")

    while True:
        second_index = choose_saved_option(travel_options, "Select second option: ")
        if second_index != first_index:
            break
        print("Please select a different second option.")

    option1 = travel_options[first_index]
    option2 = travel_options[second_index]
    result = compare_options([option1, option2])

    print("\n" + "=" * 60)
    print("TRAVEL OPTION COMPARISON")
    print("=" * 60)

    for label, option in (("Option 1", option1), ("Option 2", option2)):
        print(f"\n{label}: {option['option_name']}")
        print(f"  Total Cost      : Tk. {option['final_cost']:.2f}")
        print(f"  Cost Per Person : Tk. {option['cost_per_person']:.2f}")
        print(f"  Budget Status   : {option['budget_status']}")
        print(f"  Comfort Rating  : {option['comfort_rating']}/5")
        print(f"  Travel Time     : {option['travel_time']:.2f} hours")

    if result["cheaper"] is None:
        print("\nCheaper Option   : Both options have the same total cost.")
    else:
        print(f"\nCheaper Option   : {result['cheaper']['option_name']}")

    print(f"Cost Difference  : Tk. {result['cost_difference']:.2f}")
    print(f"Recommended      : {result['recommended']['option_name']}")
    print(f"Reason           : {result['reason']}")
    print("=" * 60)


def check_saved_plan_budget(travel_options):
    if not travel_options:
        print("\nNo saved travel plans found.")
        return

    print("\nAVAILABLE OPTIONS")
    for index, option in enumerate(travel_options, start=1):
        print(f"{index}. {option['option_name']}")

    index = choose_saved_option(travel_options, "Select an option: ")
    option = travel_options[index]

    status, difference = check_budget(option["final_cost"], option["budget"])

    print("\nBUDGET CHECK")
    print(f"Option        : {option['option_name']}")
    print(f"Final Cost    : Tk. {option['final_cost']:.2f}")
    print(f"Budget        : Tk. {option['budget']:.2f}")
    print(f"Budget Status : {status}")
    display_budget_difference(difference)


def display_main_menu():
    print("\n" + "=" * 60)
    print("TRAVEL COST PLANNER AND OPTION COMPARATOR")
    print("=" * 60)
    print("1. Create Travel Option")
    print("2. View Saved Options")
    print("3. Compare Options")
    print("4. Check Budget")
    print("5. Exit")
    print("=" * 60)


def main():
    travel_options = load_plans(FILE_NAME)

    if not travel_options:
        print("No saved travel plans found. Starting with an empty plan list.")
    else:
        print(f"Loaded {len(travel_options)} saved travel plan(s).")

    while True:
        display_main_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            new_option = create_travel_option()
            if new_option is not None:
                travel_options.append(new_option)

        elif choice == "2":
            view_saved_options(travel_options)

        elif choice == "3":
            compare_saved_options(travel_options)

        elif choice == "4":
            check_saved_plan_budget(travel_options)

        elif choice == "5":
            print("Thank you for using the Travel Cost Planner.")
            break

        else:
            print("Invalid menu choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
