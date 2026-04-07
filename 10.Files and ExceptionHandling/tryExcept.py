chai = {"masala": 10, "plain": 5, "onion": 15, "paper": 20}

# print(chai["ginger"])

try:
    print(chai["ginger"])
except KeyError:
    print("Sorry, we don't have that flavor of chai.")


def serve_chai(flavor):
    try:
        print(f"Here is your {flavor} chai. That will be {chai[flavor]} rupees.")
    except KeyError:
        print("Sorry, we don't have that flavor of chai.")

print(serve_chai("ginger"))

