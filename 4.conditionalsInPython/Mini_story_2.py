snack = input("enter your prefer snack: ").lower()

print(f"You have chosen " + snack)

if snack == "cookies" or snack == "samosa":
    print(f"great choice! {snack} are delicious.")
else :
    print(f"Sorry, we don't have {snack} in our menu.")