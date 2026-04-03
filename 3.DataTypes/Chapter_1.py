sugarAmount  = 2
print(f"initial sugar amount: {sugarAmount}")

sugarAmount = 12
print(f"initial sugar amount: {sugarAmount}")

print(f"id of 2: {id(2)}")
print(f"id of 12: {id(12)}")

#in python, integers are immutable, so when we change the value of sugarAmount, it creates a new object in memory and assigns the new value to it. The old value (2) still exists in memory, but it is not referenced by sugarAmount anymore. This is why the id of 2 and 12 are different.