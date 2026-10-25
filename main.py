"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    cost = annual_cost / SEMESTERS_PER_YEAR
    """Give back what one semester costs."""
    return cost


def cost_per_month(annual_cost):
    cost = annual_cost / MONTHS_PER_YEAR
    """Give back what one month of the academic year costs."""
    return cost


def cost_per_day(annual_cost):
    cost = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    """Give back what one class day costs."""
    return cost


def cost_per_credit(annual_cost, credits):
    cost = annual_cost / credits / 2
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost


def cost_per_class(annual_cost, credits):
    cost = (annual_cost / (credits / CS1430_CREDITS) / CS1430_MEETINGS_PER_SEMESTER)/2
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost


# ---- PROGRAM ----

def main():
    cost_per_year = float(input("Enter the total cost for one year: "))
    credits_per_year = float(input("Enter the total number of credits this semester: "))
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.

    while True:
        # Show your menu here.
        print("1 Cost per semester")
        print("2 Cost per month")
        print("3 Cost per class day")
        print("4 Cost per credit")
        print("5 Cost per CS 1430 class meeting")
        print("6 Worth it?")
        print("Q Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break

        # Add a branch for each menu option here.
        if choice == "1":
            print(f"Cost per semester: ${cost_per_semester(cost_per_year):.2f}")
        if choice == "2":
            print(f"Cost per month: ${cost_per_month(cost_per_year):.2f}")
        if choice == "3":
            print(f"Cost per class day: ${cost_per_day(cost_per_year):.2f}")
        if choice == "4":
            print(f"Cost per credit: ${cost_per_credit(cost_per_year, credits_per_year):.2f}")
        if choice == "5":
            print(f"Cost per CS 1430 class meeting: ${cost_per_class(cost_per_year, credits_per_year):.2f}")
        elif choice == "Q":
            break
        elif choice == "6":
            # Ask the user if they think college is worth it.
            answer = input("Do you think college is worth it? (yes/no): ")
            if answer.lower() == "yes":
                print("Great! Keep up the good work!")
            elif answer.lower() == "no":
                print("That's okay. College isn't for everyone.")
            else:
                print("Invalid response. Please answer 'yes' or 'no'.")

# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
