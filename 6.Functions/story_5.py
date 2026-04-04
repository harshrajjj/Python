chai = "ginger chai"

def prepare_chai(order):
    print("preparing", order, "chai")

# prepare_chai(chai)
# print(chai)

chai =[1,2,3];

def edit_chai(cup):
    cup[1] =42

# edit_chai(chai)
# print(chai)

def make_chai(tea,milk, sugar):
    print("making chai with", tea, milk, sugar)

# make_chai("green tea", "full cream", "less sugar")

# make_chai(milk="full cream", sugar="less sugar", tea="green tea")



def special_chai(*args, **kwargs):
    print("making chai with", args)
    print("extra info", kwargs)

special_chai("green tea", "full cream", "less sugar", flavor="elaichi", size="large")

# def chai_order(order = []):
#     order.append("masala")
#     print("order is", order)

def chai_order(order = None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()

