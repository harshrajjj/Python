flavours = ["ginger", "out of stock", "lemon", "discontinued", "Chocolate", "strawberry"]

for flavour in flavours:
    if flavour == "out of stock" :
        continue
    if flavour == "discontinued" :
        break
    print(f"{flavour} is available flavour")

print("We are done with the loop")


staff = [("amit", 16), ("susan", 22), ("bob", 19), ("alice", 17)]

for name, age in staff:
    if age >= 18:
        print(f"{name} is an adult")
    else:        print(f"{name} is a minor")

print("We are done with the loop")

