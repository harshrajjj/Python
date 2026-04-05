menu = [
    "Masala chai",
    "Ginger chai",
    "Lemon tea",
    "Green tea",
    "Black tea",
    "ice tea",
    "Milk tea",
]

iced_tea = [tea for tea in menu if "ice" in tea]
len_tea = [tea for tea in menu if len(tea) > 10]
print(len_tea)

print(iced_tea)


