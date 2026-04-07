class outOfIndegredient(Exception):
    pass    


def make_chai(milk, suger):
    if milk ==0 or suger ==0:
        raise outOfIndegredient("Sorry, we are out of indgredients.")
    else:
        print("Here is your chai.")

make_chai(1, 2)
make_chai(0, 2)