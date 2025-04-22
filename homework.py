class Budget:
   def __init__(self):
        self.income = []
        self.expenses = []
        self.balance = 0
   def add_income(self, amount, catagory):
        self.income.append((amount,catagory))
        self.balance += amount
   def add_expense(self, amount, catagory):
        self.expenses.append((amount, catagory))
        self.balance -= amount
   def calculate_balance(self):
        return self.balance
   def display_summary(self):
        total_income = sum(amount for amount, category in self.income)
        total_expenses = sum(amount for amount, category in self.expenses)
        print('Financal summary')
        print(f'total income: {total_income}')
        print(f'total expenses: {total_expenses}')
        print(f'Balance : {self.balance}')
        print("\n income catagory:\n")
        for amount, catagory in self.expenses:
            print(f"{catagory}: {amount}")
            print("\n income catagory:")
        for amount, catagory in self.expenses:
            print(f"{catagory}: {amount}")


my_budget = Budget()
my_budget.add_income(5000, "Salary")
my_budget.add_income(1000, "Allowance")
my_budget.add_expense(2000, "Rent")
my_budget.add_expense(1000, "Food")
my_budget.add_expense(1700, "Bills")
my_budget.add_expense(200, "Travel cost")
my_budget.add_expense(800, "Savings")
print(my_budget.calculate_balance())