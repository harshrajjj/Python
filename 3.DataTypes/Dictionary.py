chai_order = dict(type="ginger chai", size="medium", sugar_level=2)
print(f"chai order: {chai_order}")

chai_recipe = {}
chai_recipe["ginger"] = 1
chai_recipe["tea leaves"] = 2
chai_recipe["water"] = 3
print(f"chai recipe: {chai_recipe}")
print(f"chai recipe: {chai_recipe['ginger']}")

del chai_recipe["water"]
print(f"chai recipe after removing water: {chai_recipe}")

print(f"is ginger in chai recipe? {'ginger' in chai_recipe}")
print(f"is water in chai recipe? {'water' in chai_recipe}")

# print(f"orders: {chai_order.keys()}")
# print(f"values: {chai_order.values()}")
# print(f"items: {chai_order.items()}")

last_item = chai_order.popitem()
print(f"last item: {last_item}")
print(f"chai order after removing last item: {chai_order}")

extra_order = {"flavor": "spicy", "temperature": "hot"}
chai_order.update(extra_order)
print(f"chai order after adding extra order: {chai_order}")

chai_size = chai_order.get("size", "unknown")#the get method is used to retrieve the value associated with the key "size" from the chai_order dictionary. If the key "size" does not exist in the dictionary, it will return the default value "unknown" instead of raising a KeyError. In this case, since "size" is a key in the chai_order dictionary, it will return the value "medium".
print(f"chai size: {chai_size}")

