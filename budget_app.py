class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append(
            {'amount': amount, 'description': description}
        )

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item['amount']
        return total

    def transfer(self, amount, destination_category):
        withdrawal_description = f"Transfer to {destination_category.name}"

        if self.check_funds(amount):
            self.withdraw(amount, withdrawal_description)
            deposit_description = f"Transfer {self.name}"

            destination_category.deposit(amount, deposit_description)
            return True
        return False
    

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def __str__(self):

        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            amount = f"{entry['amount']:>7.2f}"
            description = entry['description'][:23]
            items += f"{description:<23}{amount:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total
    
def create_spend_chart(categories):
    pass

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

    # print( food.deposit(900, 'deposit') and food.withdraw(45.67, 'milk, cereal, eggs, bacon, bread') )