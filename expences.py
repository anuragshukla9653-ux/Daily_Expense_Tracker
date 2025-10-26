# Daily Expense Tracker
# Uses file writing and simple input/output

import os

FILE_NAME = "expenses.txt"

# Function to add a new expense
def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (e.g., Food, Travel, Shopping): ")
    amount = input("Enter amount (in ₹): ")
    description = input("Enter short description: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")

    print("✅ Expense added successfully!\n")

# Function to view all expenses
def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("📭 No expenses found yet.\n")
        return

    print("\n📒 All Expenses:")
    print("-" * 50)

    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            # Handle lines safely (in case of extra commas)
            if len(parts) < 4:
                continue
            date = parts[0]
            category = parts[1]
            amount = parts[2]
            description = ",".join(parts[3:])  # join remaining parts
            print(f"{date} | ₹{amount} | {category} | {description}")

    print("-" * 50 + "\n")


# Function to show summary (total and by category)
def show_summary():
    if not os.path.exists(FILE_NAME):
        print("📭 No expenses to summarize.\n")
        return

    total = 0
    category_total = {}

    with open(FILE_NAME, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 3:
                continue
            category = parts[1]
            try:
                amount = float(parts[2])
            except ValueError:
                continue
            total += amount
            category_total[category] = category_total.get(category, 0) + amount

    print("\n📊 Expense Summary:")
    print("-" * 50)
    print(f"💰 Total Spent: ₹{total}")
    print("\nBy Category:")
    for cat, amt in category_total.items():
        print(f"   • {cat}: ₹{amt}")
    print("-" * 50 + "\n")


# Function to clear all expenses
def clear_expenses():
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("🧹 All expenses cleared.\n")
    else:
        print("No file found.\n")

# Main menu
def main():
    while True:
        print("=== 💵 Daily Expense Tracker ===")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Show Summary")
        print("4. Clear All Expenses")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            clear_expenses()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-5.\n")

# Run program
if __name__ == "__main__":
    main()
