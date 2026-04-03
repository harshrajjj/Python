cup_size = input("Enter your cup size (small, medium, large): ").lower()

if cup_size == "small":
    print("You have chosen a small cup. It will hold 250ml of tea.")
elif cup_size == "medium":
    print("You have chosen a medium cup. It will hold 500ml of tea.")
elif cup_size == "large":
    print("You have chosen a large cup. It will hold 1000ml of tea.")
else:
    print("Invalid cup size. Please choose from 'small', 'medium', or 'large'.")