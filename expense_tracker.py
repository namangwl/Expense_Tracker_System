# Simple Python script to track expenses and budget
# Written for portfolio project

print("--- Corporate Expense & Budget Tracker ---")
print("Tip: Keep track of your spending so you don't cross the limit!\n")

# Step 1: Set the initial monthly budget
try:
    my_budget = float(input("What is your total budget for this month? (in Rs): "))
except ValueError:
    # If user types letters instead of numbers, catch the error and set a default
    print("Oops! That doesn't look like a number. Setting a default budget of Rs. 10000.")
    my_budget = 10000.0

# Step 2: Create variables to store our data
total_spent = 0
expenses = []  # This empty list will hold all our expense entries (like a digital diary)

# Step 3: Run a loop to keep asking for expenses until the user is done
while True:
    print("\nWhat do you want to do?")
    print("1. Add a new expense")
    print("2. Finish and see my report")
    
    user_choice = input("Enter 1 or 2: ")
    
    if user_choice == '1':
        item = input("Where did you spend? (e.g., Servers, Ads, Travel): ")
        try:
            cost = float(input(f"How much did you spend on {item}? Rs. "))
            
            # Add the cost to our total, and save the details in our list
            total_spent += cost
            expenses.append({"name": item, "cost": cost})
            
            print(f"✅ Added! You have Rs. {my_budget - total_spent} left.")
            
        except ValueError:
            print("❌ Invalid amount! Please enter a number for the cost.")
            
    elif user_choice == '2':
        # User wants to exit, so we break the loop
        print("Stopping the tracker...\n")
        break 
        
    else:
        # If user types 3, 4 or abc
        print("❌ Wrong choice. Please strictly type 1 or 2.")

# Step 4: Generate and show the final summary report
print("========================================")
print("          FINAL EXPENSE REPORT          ")
print("========================================")

# Loop through our diary (list) and print all items one by one
if len(expenses) == 0:
    print("No expenses recorded yet.")
else:
    for entry in expenses:
        print(f"- {entry['name']}: Rs. {entry['cost']}")

print("----------------------------------------")
print(f"Total Initial Budget : Rs. {my_budget}")
print(f"Total Amount Spent   : Rs. {total_spent}")

# Logical check: Did we cross the limit?
if total_spent > my_budget:
    overspent = total_spent - my_budget
    print(f"⚠️ WARNING: You crossed your budget by Rs. {overspent}!")
else:
    saved = my_budget - total_spent
    print(f"✅ GREAT JOB: You stayed in budget and saved Rs. {saved} this month.")
print("========================================")
