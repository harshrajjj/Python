class baseChai:
    def __init__(self, flavor):
        self.flavor = flavor

    def describe(self):
        print(f"This is a {self.flavor} chai.")


class chaiOrder(baseChai):
    def __init__(self, flavor):
        super().__init__(flavor)

    def order_summary(self):
        print(f"Your order {self.flavor} chai.")


    
class cahiShop:
    cahi_cls = baseChai

    def __init__ (self):
        self.cahi = self.cahi_cls("masala")


    def serve(self):
        print(f"Serving {self.cahi.flavor} chai.")
        self.cahi.describe()
        self.cahi.order_summary()

class fancyChaiShop(cahiShop):
    cahi_cls = chaiOrder

shop = fancyChaiShop()
shop.serve()