def make_chai():
    return "masala chai"

# print(make_chai())


def ideal_chai():
    pass

# print(ideal_chai())



def chai_status(cups):
    if cups > 3:
        return "too much chai"
    elif cups == 3:
        return "just right"
    else:
        return "not enough chai"

# print(chai_status(4))

def chai_report():
    return 100,20,10

sold , remaining ,_ = chai_report()
print("sold", sold, "remaining", remaining)