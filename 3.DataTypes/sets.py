essential_spices = {"salt", "pepper", "cumin","cinnamon"}
optional_spices = {"ginger", "cardamom", "cinnamon"}

all_spices = essential_spices | optional_spices
print(f"all spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

only_essential_spices = essential_spices - optional_spices
print(f"only essential spices: {only_essential_spices}")

#member testing
print(f"is cumin an essential spice? {'cumin' in essential_spices}")
print(f"is ginger an essential spice? {'ginger' in essential_spices}")
print(f"is ginger an optional spice? {'ginger' in optional_spices}")
print(f"is turmeric an essential spice? {'turmeric' in essential_spices}")
print(f"is turmeric an optional spice? {'turmeric' in optional_spices}")

