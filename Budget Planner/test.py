import budget
outgoings = budget.BudgetManager(float(input('How much money do you have '
                                             'available? ')))
answer = input('Do you want to add a budget? y/n ')
while answer == "y":
    budget_name = input("What is the name of your budget? ")
    outgoings.add_budget(budget_name, float(input(f'What is your '
                                                  '{budget_name} budget? ')))
    answer = input('Do you want to add any more budgets? y/n ')
outgoings.print_summary()
answer = input('Do you want to change any of your budgets? y/n ')
while answer == "y":
    budget_name = input('Which budget do you want to change? ')
    if budget_name in outgoings.budgets:
        outgoings.change_budget(budget_name, float(input(f'What is '
                                                         f'the new '
                                                         f'{budget_name} '
                                                         f'budget? ')))
    else:
        print("You do not have a budget with that name.")
    answer = input('Do you want to change any other budget? y/n ')
answer = input('Do you want to record any expenditures? y/n ')
while answer == "y":
    expenditure_name = input('From which budget are the expenditures? ')
    if expenditure_name in outgoings.budgets:
        outgoings.spend(expenditure_name, float(input(f'How much did '
                                                      f'you spend in '
                                                  f'{expenditure_name}?')))
    else:
        print("You do not have a budget with that name.")
    answer = input('Do you want to record any more expenditures? y/n ')
outgoings.print_summary()
