def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    
    with open("expenses.txt", "a") as file:
        file.write(f"{name},{amount}\n")
    
    print("Expense added successfully!")

def view_expenses():
    try:
        with open("expenses.txt", "r") as file:
            total = 0
            for line in file:
                name, amount = line.strip().split(",")
                print(f"{name}: ₹{amount}")
                total += float(amount)
            
            print(f"\nTotal Expenses: ₹{total}")
    except FileNotFoundError:
        print("No expenses found!")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid choice!")
