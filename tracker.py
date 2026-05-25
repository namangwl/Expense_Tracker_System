# Personal Expense Tracker
# Uses Python While Loops and If-Else conditions

print("=== DAILY EXPENSE TRACKER ===")
print("Type 'stop' in item name when you are done adding expenses.\n")

expenses = []
total_amount = 0

while True:
    item_name = input("Enter expense item: ")
    
    if item_name.lower() == 'stop':
        break
        
    amount_str = input("Enter amount: ")
    amount = float(amount_str)
    
    category = input("Enter category (Food/Travel/Other): ")
    
    if amount < 0:
        print("Amount cannot be negative! Try again.\n")
        continue 
        
    expenses.append({
        "item": item_name,
        "amount": amount,
        "category": category
    })
    
    total_amount += amount
    print(f"Added {item_name} successfully!\n")

print("\n--- EXPENSE SUMMARY ---")
if len(expenses) == 0:
    print("No expenses recorded today.")
else:
    for exp in expenses:
        print(f"-> {exp['item']} ({exp['category']}) : Rs.{exp['amount']}")
        
    print("-----------------------")
    print(f"TOTAL SPENT : Rs.{total_amount}")

    if total_amount > 1000:
        print("Warning: You are spending a lot today!")
    else:
        print("Great! You are within budget.")
