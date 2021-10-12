class Category:
    def __init__(self, name):
        self.name = name
        self.total = 0.0
        self.ledger = []

    def __repr__(self):
        s = f"{self.name:*^30}\n"
        acc = 0

        for item in self.ledger:
            s += f"{item['description']}{item['amount']:>{30 - len(item['description'])}}\n"
            acc += item['amount']

            s += f"Total: 123"
            return s

    def deposit(self, amount, description):
        self.total += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, *args):
        can_withdraw = self.check_funds(amount)

        description = args[0] if args else ""

        if can_withdraw:
            self.total -= amount
            self.ledger.append({"amount": -amount, "description": description})

        return can_withdraw

    def get_balance(self):
        return self.total

    def transfer(self, amount, instance):
        can_transfer = self.check_funds(amount)

        if can_transfer:
            self.withdraw(amount, f"Transfer to {instance.name}")
            instance.deposit(amount, f"Transfer from {self.name}")

        return can_transfer

    def check_funds(self, amount):
        if amount > self.total:
            return False
        return True


food = Category("Food")
entertainment = Category("Entertainment")
food.deposit(100, "something")
food.transfer(25.5, entertainment)


# food.withdraw(20, "beans")
# print(food.ledger)
# print(str(food))
# print(entertainment.ledger)
# print(food.get_balance())
# print(entertainment.get_balance())


def create_spend_chart(categories):
    s = "Percentage spent by category\n"

    total = 0
    cats = {}
    for cat in categories:
        cat_total = 0
        for item in cat.ledger:
            amount = item["amount"]
            if amount < 0:
                total += amount
                cat_total += amount

        cats[cat.name] = abs(cat_total)

    total = abs(total)

    for key, val in cats.items():
        percent = (val / total) * 100
        cats[key] = percent

    print(cats)

    for n in range(100, -1, -10):
        s += f"{str(n) + '|':>4}"
        for val in cats.values():
            if val >= n:
                s += " o"
        s += "\n"

    L = len(cats.values())
    s += f"    {(L * 3 + 1) * '_'}\n"

    i = 0
    while True:
        try:
            temp_str = ""
            for key in cats.keys():
                temp_str += key[i]
            i += 1
            s += f"     {temp_str}\n"
        except:
            break

    print(s)


create_spend_chart([food, entertainment])







