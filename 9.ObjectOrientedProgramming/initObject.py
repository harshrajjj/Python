class chaiOrder:
    def __init__(self, flavor):
        self.flavor = flavor

    def summery(self):
        print(f"Your order is {self.flavor} chai.")

    def __str__(self):
        return f"this is a {self.flavor} chai"
    

order1 = chaiOrder("ginger")
order1.summery()
print(order1)

order2 = chaiOrder("matcha")
order2.summery()
print(order2)