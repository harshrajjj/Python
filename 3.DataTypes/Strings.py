ChaiType = "ginger chai"
CustomerName = "Alice"

print(f"Customer {CustomerName} ordered a cup of {ChaiType}.")

chaiDescription = "Aromatic and bold" #last number is not inclusive in python, so it will print up to index 9
print(f"First 10 characters of chai description: {chaiDescription[0:10]}")
#in python, strings are immutable, so when we create a new string by slicing or concatenating, it creates a new object in memory rather than modifying the existing one. This is why the id of chaiDescription remains the same even after we create a new string from it.

print(f"last word:{chaiDescription[::-1]}") #reverses the string

label_text = "Ginger Chai"
encode_lavel = label_text.encode("utf-8")
print(f"non encoded label: {label_text}")
print(f"encoded label: {encode_lavel}")

decode_level = encode_lavel.decode("utf-8")
print(f"decoded label: {decode_level}")
