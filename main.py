import datetime

def add_expense():
    name = input("Enter expense name: ")
    category = input("Enter category (Food/Travel/Other): ")
    amount = float(input("Enter amount: "))
    
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("expenses.txt", "a") as file:
        file.write(f"{name},{category},{amount},{date}\n")
    
    print("Expense added successfully!")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            total = 0
            print("\n--- Your Expenses ---")
            
            for line in file:
                name, category, amount, date = line.strip().split(",")
                print(f"{date} | {name} ({category}): ₹{amount}")
                total += float(amount)
            
            print(f"\nTotal Expenses: ₹{total}")
    
    except FileNotFoundError:
        print("No expenses found!")

def monthly_total():
    try:
        month = input("Enter month (YYYY-MM): ")
        total = 0
        
        with open("expenses.txt", "r") as file:
            for line in file:
                name, category, amount, date = line.strip().split(",")
                if date.startswith(month):
                    total += float(amount)
        
        print(f"Total expenses for {month}: ₹{total}")
    
    except FileNotFoundError:
        print("No data found!")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Monthly Total")
    print("4. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        monthly_total()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Please try again.")
