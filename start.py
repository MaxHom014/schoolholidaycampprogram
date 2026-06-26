# List of camp options holding names, durations, and base costs
camps = [
    {"name": "Cultural Immersion", "days": 5, "cost": 800},
    {"name": "Kayaking and Pancakes", "days": 3, "cost": 400},
    {"name": "Mountain Biking", "days": 4, "cost": 900}
]

# List of available meal options
meals = ["Standard", "Vegetarian", "Vegan"]

# Constant for the flat-rate shuttle bus option
SHUTTLE_COST = 80


def get_name():
    """Get and validate participant name."""
    while True:
        name = input("What is your name? ").strip()

        if name == "":
            print("Name cannot be blank.")
        elif not name.replace(" ", "").isalpha():
            print("Name must contain letters only.")
        else:
            return name.title()


def get_age():
    """Get and validate age."""
    while True:
        try:
            age = int(input("Enter your age (5-17): "))

            if 5 <= age <= 17:
                return age
            else:
                print("Age must be between 5 and 17.")

        except ValueError:
            print("Age must be a number.")


def get_camp():
    """Display camps and return selected camp."""
    print("\nCamp Options:")
    for i, camp in enumerate(camps, start=1):
        print(f"{i}. {camp['name']} ({camp['days']} days) - ${camp['cost']}")

    while True:
        try:
            choice = int(input("Choose a camp (1-3): "))

            if 1 <= choice <= len(camps):
                return camps[choice - 1]
            else:
                print("Invalid camp number.")
        except ValueError:
            print("Please enter a number.")


def get_shuttle():
    """Ask whether shuttle is required."""
    while True:
        shuttle = input("Do you need the shuttle bus? (yes/no): ").strip().lower()

        if shuttle in ["yes", "y"]:
            return True
        elif shuttle in ["no", "n"]:
            return False
        else:
            print("Please enter yes or no.")


def get_meal():
    """Display meal options and return selected meal."""
    print("\nMeal Options:")
    for i, meal in enumerate(meals, start=1):
        print(f"{i}. {meal}")

    while True:
        try:
            choice = int(input("Choose a meal option: "))

            if 1 <= choice <= len(meals):
                return meals[choice - 1]
            else:
                print("Invalid meal choice.")
        except ValueError:
            print("Please enter a number.")


# Main Program
name = get_name()
age = get_age()
camp = get_camp()
shuttle = get_shuttle()
meal = get_meal()

# Calculate total cost
total_cost = camp["cost"]

if shuttle:
    total_cost += SHUTTLE_COST

# Print summary
print("\nBooking Summary")
print("Name:", name)
print("Age:", age)
print("Camp:", camp["name"])
print("Duration:", camp["days"], "days")
print("Meal:", meal)
print("Shuttle:", "Yes" if shuttle else "No")
print("Total Cost: $", total_cost)

# Confirm attendance
confirm = input("\nDo you want to confirm your booking? (yes/no): ").strip().lower()

if confirm in ["yes", "y"]:
    print(f"Thank you {name}! Your booking has been confirmed.")
else:
    print("Your booking has not been confirmed.")