# Capstone Project: Personal Finance Tracker
# Neha Rao


expenses = {}      # empty dictionary for expenses


def add_expense(expenses):      # Function to add expenses
    try:
        # Get the expense description from user
        description = input("Enter expense description: ")
        if not description:
            print("Description cannot be empty.")
            return
        
        # Get expense category from user
        category = input("Enter category: ")
        if not category:
            print("Category cannot be empty.")
            return
        
        # Get expense amount from user
        amount_input = input("Enter amount: ")
        amount = float(amount_input)
        if amount < 0:
            print("Amount cannot be negative.")
            return
        
        # Add expense to dictionary, creates new category if doesn't already exist
        expenses.setdefault(category, []).append((description, amount))
        print("Expense added successfully.")

    except ValueError:
        print("Invalid amount. Please enter a number.")
    except Exception as e:
        print(f"Unexpected error: {e}")



def view_expenses(expenses):        # Function to view expenses
    if expenses:        # Check if expenses dictionary is not empty
        for category, items in expenses.items():        # Loop through each category
            print(f"Category: {category}")
            for description, amount in items:       # Loop through each expense in category
                print(f"  - {description}: ${amount:.2f}")

    else:       # If expenses dictionary is empty
        print("No expenses recorded yet.")
        return




def view_summary(expenses):     # Function to view summary
    if expenses:        # Check if expenses dictionary is not empty
        print("Summary:")

        for category, items in expenses.items():        # Loop through each category
            total = 0
            for amount in items:        # Loop through each expense in category and sum up the amounts
                total += amount[1]
            print(f"{category}: ${total:.2f}")

    else:       # If expenses dictionary is empty
        print("No expenses recorded yet.")
        return




# Loop until user chooses to exit
print("\nWelcome to the Personal Finance Tracker!")
while True:
    print("What would you like to do?")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Summary")
    print("4. Exit")
    userChoice = input("Choose an option: ")
    print("\n")

    if userChoice == "1":       # Add Expense
        add_expense(expenses)

    elif userChoice == "2":     # View All Expenses
       view_expenses(expenses)

    elif userChoice == "3":     # View Summary
        view_summary(expenses)

    elif userChoice == "4":     # Exit
        print("Exiting program...")
        break

    else:       # Invalid choice
        print("\nInvalid choice. Please try again.")
    

    print("\n\n")


print("Thank you for using the Personal Finance Tracker!\nGoodbye! 👋")

