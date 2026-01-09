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
            deposit_description = f"Transfer from {self.name}"

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
    title = "Percentage spent by category\n"
    
    
    # Calculate total spent and spending per category
    spent_amounts = []
    for category in categories:
        total = 0
        for item in category.ledger:
            if item['amount'] < 0:
                total += abs(item['amount'])
        spent_amounts.append(total)
    
    total_spent = sum(spent_amounts)
    
    spent_percentages = [(amount / total_spent) * 100 // 10 * 10 for amount in spent_amounts]
    
    chart = ""
    for i in range(100, -1, -10):
        line = f"{i:>3}|"
        for percent in spent_percentages:
            if percent >= i:
                line += " o "
            else:
                line += "   "
        chart += line + " \n"
    
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    names = [c.name for c in categories]
    max_len = max(len(name) for name in names)
    for i in range(max_len):
        line = "     "
        for name in names:
            if i < len(name):
                line += name[i] + "  "
            else:
                line += "   "
        if i < max_len - 1:
            line += "\n"
        chart += line
        
    return title + chart
    

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)

entertainment = Category("Entertainment")
entertainment.deposit(500, "deposit")
entertainment.withdraw(33.40, "movie and snacks")


business = Category("Business")
business.deposit(1000, "deposit")
business.withdraw(10.99, "office supplies")


print(food)


print(create_spend_chart([food, clothing, entertainment, business]))
    