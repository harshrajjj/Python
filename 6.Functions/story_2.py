def get_input():
    print("getting user input")

def validate_input():
    print("validating user input")

def save_input():
    print("saving user input")

def register_user():
    get_input()
    validate_input()
    save_input()
    print("registering user")

# register_user()


def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

mybill = calculate_bill(3, 5)
# print(mybill)



def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100,150,200]

for order in orders:
    total_price = add_vat(order, 20)
    print(f"original price:", order, "total price with VAT:", total_price)
    