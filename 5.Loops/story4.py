menu = ["chai", "coffee", "milk", "juice"]

# for m in menu:
#     print(f"preparing {m} for customer")

for idx, item in enumerate(menu, start=1):
    print(f"preparing {item} for customer #{idx}")