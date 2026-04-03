masala_spices = ("cumin", "coriander", "cardamom", "cloves", "cinnamon")
print(f"masala spices: {masala_spices}")

(spice1, spice2, spice3, spice4, spice5) = masala_spices
print(f"spice 1: {spice1}")
print(f"spice 2: {spice2}")
print(f"spice 3: {spice3}")

gingerRatio, turmericRatio, cuminRatio, corianderRatio, cardamomRatio = (0.2, 0.3, 0.1, 0.25, 0.15)
print(f"ginger ratio: {gingerRatio}")
print(f"turmeric ratio: {turmericRatio}")
print(f"cumin ratio: {cuminRatio}")

gingerRatio, turmericRatio = turmericRatio, gingerRatio#swapping values of gingerRatio and turmericRatio


# member testing

print(f"is ginger in masala spices? {'ginger' in masala_spices}")
print(f"is cumin in masala spices? {'cumin' in masala_spices}")