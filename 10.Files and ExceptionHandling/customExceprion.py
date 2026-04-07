def brew_chai(flavor):
    if flavor not in ["masala", "plain", "onion", "paper"]:
        raise ValueError("Sorry, we don't have that flavor of chai.")
    else:
        print(f"Here is your {flavor} chai.")

try:
    brew_chai("ginger")
except ValueError as e:
    print(e)

print(brew_chai("ginger"))
print(brew_chai("masala"))
print(brew_chai("plain"))
print(brew_chai("onion"))
print(brew_chai("paper"))
print(brew_chai("ginger"))