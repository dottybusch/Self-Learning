available = 2500.00
budgets = {}
expenditure = {}

def add_budget(name, amount):
    global available #makes "available" a global variable in all functions
    if name in budgets:
        raise ValueError("Budget exists")
    if amount > available:
        raise ValueError("Insufficient funds")
    budgets[name] = amount
    available -= amount
    expenditure[name] = 0
    return available

def spend(name, amount):
    if name not in expenditure:
        raise ValueError("No such budget")
    expenditure[name] += amount
    budgeted = budgets[name]
    spent = expenditure[name]
    return budgeted - spent

def print_summary():
    print("Budget            Budgeted      Spent  Remaining")
    print("--------------- ---------- ---------- ----------")
    total_budgeted = 0
    total_spent = 0
    total_remaining = 0
    for name in budgets:
        budgeted = budgets[name]
        spent = expenditure[name]
        remaining = budgeted - spent
        print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}')
        total_budgeted += budgeted
        total_spent += spent
        total_remaining += remaining
    print("--------------- ---------- ---------- ----------")
    print(f'{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f} '
          f'{total_budgeted - total_spent:10.2f}')
