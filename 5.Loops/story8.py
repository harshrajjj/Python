#warlus

# value  = 13
# remainder = value % 5

# if remainder :
#     print(f"not a multiple of 5, remainder is {remainder}")

value = 15

if (remainder := value % 5) :#walrus operator
    print(f"not a multiple of 5, remainder is {remainder}")


avilable_size = ["small", "medium", "large"]

if((requested_size := input("what size do you want?") )in avilable_size):
    print(f"{requested_size} is available")
else:    print(f"{requested_size} is not available")



flavours = ["ginger", "masala", "lemon", "mint"]
print(flavours)

while (flavour := input("what flavour do you want?") ) not in flavours:
    print(f"{flavour} is not available, please choose another flavour")

print(f"{flavour} is available")