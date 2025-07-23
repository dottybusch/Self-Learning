class BudgetManager:
    def __init__(self, amount):
        self.available = amount
        self.budgets = {}
        self.expenditure = {}

    def add_budget(self, name, amount):
        if name in self.budgets:
            raise ValueError("Budget exists")
        if amount > self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = amount
        self.expenditure[name] = []
        self.available -= amount
        return self.available

    def change_budget(self, name, new_amount):
        if name not in self.budgets:
            raise ValueError("Budget does not exist")
        old_amount = self.budgets[name]
        if new_amount > old_amount + self.available:
            raise ValueError("Insufficient funds")
        self.budgets[name] = new_amount
        self.available -= new_amount - old_amount
        return self.available

    def spend(self, name, amount):
        if name not in self.expenditure:
            raise ValueError("No such budget")
        self.expenditure[name].append(amount)
        budgeted = self.budgets[name]
        spent = sum(self.expenditure[name])
        return budgeted - spent

    def print_summary(self):
        print("\nBudget            Budgeted      Spent  Remaining")
        print("--------------- ---------- ---------- ----------")
        total_budgeted = 0
        total_spent = 0
        total_remaining = 0
        for name in self.budgets:
            budgeted = self.budgets[name]
            spent = sum(self.expenditure[name])
            remaining = budgeted - spent
            print(f'{name:15s} {budgeted:10.2f} {spent:10.2f} {remaining:10.2f}')
            total_budgeted += budgeted
            total_spent += spent
            total_remaining += remaining
            money_left = self.available
        print("--------------- ---------- ---------- ----------")
        print(f'{"Total":15s} {total_budgeted:10.2f} {total_spent:10.2f} '
              f'{total_budgeted - total_spent:10.2f}')
        print("\nNon-budgeted amount:" f'{money_left:10.2f}')
        print("----------------------------------")
        print("\nExpenditures:")
        for key, value in self.expenditure.items():
            print(f'{key}:')
            print(f'{value}')
            

