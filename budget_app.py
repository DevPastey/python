class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append(
            {'amount': amount, 'description': description}
        )

    def withdraw(self, amount, description=""):
        if amount > 0:
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return self.ledger

    def transfer(self, amount, destination_category):
        withdrawal_description = f"Transfer to {destination_category.name}"
        
        if self.withdraw(amount, withdrawal_description):

            deposit_description = f"Transfer {self.name}"

            destination_category.deposit(amount, deposit_description)
            return True
        return False
    

    def check_funds(self, amount):
        if amount > self.leger:
            return False
        return True

    def __str__(self):

        title_line = f"{'*' * ((30 - len(self.name)) // 2)}{self.name}{'*' * ((30 - len(self.name)) // 2)} \ninitial"
        # Ledger entries, left-aligned description and right-aligned amount (2 decimal places)
        ledger_lines = ""
        for transaction in self.ledger:
            description = transaction['description'][:23]  # Description max 23 characters
            amount = f"{transaction['amount']:>7.2f}"  # Right-align amount, 2 decimal places
            ledger_lines += f"{description:<23}{amount}\n"

        # Final balance line
        total_balance = f"Total: {self.get_balance():.2f}"

        # Combine everything
        return f"{title_line}\n{ledger_lines}{total_balance}"



def create_spend_chart(categories):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

# Print categories after transactions
print(food)

    # print( food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread') )