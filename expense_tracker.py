from expense import Expense
def main():
    print("meow")
    pass
    expense_file_path = "expenses.csv"
    # Get user to input expense.
    expense = get_user_expense()
    print(expense)
    # Write expense to a filecat
    save_expense_to_file(expense, expense_file_path)
    # Read the file and summarize their expenses.
    summarize_expense(expense_file_path)

def get_user_expense():
    print("Getting user expense")
    expense_name = input("Enter expense name: ")
    expense_amt = float(input("Enter expense amount: "))
    print(f"You've entered: {expense_name}, {expense_amt}")

    expense_categories = [
        "Food",
        "Groceries",
        "Transport",
        "Rent",
        "Fun",
        "Misc."
    ]

    while True:
        print("Select a category: ")
        for i, category in enumerate(expense_categories):
            print(f"{i + 1}. {category}")
        value_range = f"[1 - {len(expense_categories)}]"
        selected_index =int(input(f"Enter category number {value_range}: ")) - 1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amt)
            return  new_expense
        else:
            print("Invalid category. Please try again!")


def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"Saving user expense {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")


def summarize_expense(expense_file_path):
    print("Summarizing user expense")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            stripped_line = line.strip()
            expense_name, expense_category, expense_amount = stripped_line.split(",")
            line_expense = Expense(expense_name, expense_category, float(expense_amount))
            expenses.append(line_expense)
    
    

if __name__ == "__main__":
    main()