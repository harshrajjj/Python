def pure_chai(cups):
    return cups * 5


total_chai =0

#not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups * 5
    

def pore_chai(n):
    if n == 0:
        return "All cupos are served"
    else:
        return pore_chai(n-1)
    
# print(pore_chai(5))


chai_types = ["masala", "ginger", "lemon","masala", "ginger", "lemon"]

strong_chai = list(filter(lambda chai: chai == "masala", chai_types))
# print(strong_chai)

