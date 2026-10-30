import matplotlib.pyplot as plt

GOAL = 10000

steps_list = []
calories_list = []


def get_whole_number(text):
    """Return a non-negative whole number or None if input is invalid."""
    text = text.strip()
    if text.isdigit():
        return int(text)
    return None


def get_positive_number(text):
    """Return a positive float or None if input is invalid."""
    try:
        value = float(text)
    except ValueError:
        return None
    if value > 0:
        return value
    return None


def add_record():
    steps = get_whole_number(input("Steps: "))
    if steps is None:
        print("Invalid steps. Enter a non-negative whole number. Record not saved.")
        return

    calories = get_whole_number(input("Calories: "))
    if calories is None:
        print("Invalid calories. Enter a non-negative whole number. Record not saved.")
        return

    steps_list.append(steps)
    calories_list.append(calories)

    day = len(steps_list)
    percent = steps / GOAL * 100
    if steps >= GOAL:
        achieved = "Yes"
    else:
        achieved = "No"
    print(f"Record saved for Day {day}. Goal achieved: {achieved} ({percent:.2f}% of goal)")


def average_steps():
    return sum(steps_list) / len(steps_list)


def total_calories():
    return sum(calories_list)


def best_day():
    best_steps = max(steps_list)
    day = steps_list.index(best_steps) + 1
    return day, best_steps


def goal_days():
    count = 0
    for s in steps_list:
        if s >= GOAL:
            count += 1
    return count


def show_summary():
    if len(steps_list) == 0:
        print("No records yet. Please add a record first.")
        return

    day, best = best_day()
    print(f"Average steps: {average_steps():.2f} | "
          f"Total calories: {total_calories()} | "
          f"Best day: Day {day} ({best} steps) | "
          f"Goal days: {goal_days()}/{len(steps_list)}")


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def show_bmi():
    weight = get_positive_number(input("Weight (kg): "))
    if weight is None:
        print("Invalid weight. Enter a positive number.")
        return

    height = get_positive_number(input("Height (m): "))
    if height is None:
        print("Invalid height. Enter a positive number.")
        return

    bmi = calculate_bmi(weight, height)
    print(f"BMI: {bmi:.2f} | Category: {bmi_category(bmi)}")


def show_chart():
    if len(steps_list) == 0:
        print("No records yet. Please add a record first.")
        return

    days = ["Day " + str(i) for i in range(1, len(steps_list) + 1)]

    plt.bar(days, steps_list, color="skyblue", label="Steps")
    plt.axhline(y=GOAL, color="red", linestyle="--", label="Goal (10000)")
    plt.title("Daily Steps")
    plt.xlabel("Day")
    plt.ylabel("Steps")
    plt.legend()
    plt.show()
    print("Bar chart 'Daily Steps' displayed")


def main():
    while True:
        print("\n--- Fitness Data Tracker ---")
        print("1. Add record")
        print("2. Summary")
        print("3. BMI")
        print("4. Chart")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_record()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            show_bmi()
        elif choice == "4":
            show_chart()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


main()
