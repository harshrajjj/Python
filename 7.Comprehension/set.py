favroute_cahi = [
    "masala chai",
    "masala chai",
    "ginger chai",
    "lemon tea",
    "lemon tea",
    "green tea",
    "green tea",
    "black tea",
    "ice tea",
    "milk tea",
    "milk tea",
]


unique_chai = {tea for tea in favroute_cahi}
print(unique_chai)


recipe = {
    "masala chai": ["tea leaves", "milk", "sugar", "spices"],
    "ginger chai": ["ginger", "water"],
    "lemon tea": ["lemon juice", "water"],
    "green tea": ["green tea bag", "water"],
    "black tea": ["black tea bag", "water"],
    "ice tea": ["water", "ice"],
    "milk tea": ["milk", "water"],
}

unipue_ingredients = {spice for ingredients in recipe.values() for spice in ingredients} # nested comprehension
print(unipue_ingredients)

