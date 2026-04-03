spiceMix = set()
print(f"spice mix id is : {id(spiceMix)}")

spiceMix.add("ginger")
print(f"spice mix id is : {id(spiceMix)}")

spiceMix.add("cumin")
print(f"spice mix id is : {id(spiceMix)}")

spiceMix.add("turmeric")
print(f"spice mix id is : {id(spiceMix)}")

#in python, sets are mutable, so when we add an element to the set, it modifies the existing object in memory rather than creating a new one. This is why the id of spiceMix remains the same even after we add new elements to it.