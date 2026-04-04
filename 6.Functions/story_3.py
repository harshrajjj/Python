def serve_chai():
    cahi_type = "masala chai"
    print(f"inside function: serving {cahi_type} chai")


cahi_type = "ginger chai"
serve_chai()
print(f"outside function: serving {cahi_type} chai")

def chai_counter():
    chai_order = "lemon"
    def print_order():
        chai_order = "masala"
        print("inner", chai_order)
    print_order()
    print("outer:", chai_order)

chai_counter()