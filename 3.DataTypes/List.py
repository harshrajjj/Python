#mutable 

ingredients = ["water" , "milk", "black tea"]

print(f"ingredient are :{ingredients}")
ingredients.remove("water")
print(f"ingredient are : {ingredients}")

spiceaOptions = ["ginger", "cardamom"]
chaiaindegrent = ["water", "milk"]

chaiaindegrent.extend(spiceaOptions)
print(f"chai: {chaiaindegrent}")

chaiaindegrent.insert(2, "blacktea")

print(f"chai: {chaiaindegrent}")

last_added = chaiaindegrent.pop()

print(f"{last_added}")
print(f"chai: {chaiaindegrent}")
chaiaindegrent.reverse()
print(f"chai: {chaiaindegrent}")
chaiaindegrent.sort()
print(f"chai: {chaiaindegrent}")

suger_level = [1,2,3,4,5]
print(f"maximum suger level:{max(suger_level)}")
print(f"minimum suger level:{min(suger_level)}")

base_liquid = ["water", "milk"]
additional_ingredients = ["black tea", "ginger", "cardamom"]

full_ingredients = base_liquid + additional_ingredients
print(f"full ingredients: {full_ingredients}")

strong_ingredients = ["blacktea"] * 2
print(f"strong ingredients: {strong_ingredients}")

raw_spices = bytearray(b"cumin")#creating a bytearray object called raw_spices with the initial value of the byte string "cumin". The b prefix indicates that the string is a byte literal, and the bytearray function converts it into a mutable sequence of bytes.

raw_spices = raw_spices.replace(b"cumin", b"coriander")#replacing the byte sequence "cumin" with "coriander" in the raw_spices bytearray. The replace method creates a new bytearray with the specified replacements and assigns it back to raw_spices.

print(f"raw spices: {raw_spices}")
raw_spices