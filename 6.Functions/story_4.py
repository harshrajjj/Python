def update_order():
    chai_type =" Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "kesar"
    kitchen()
    print("after kitchen update", chai_type)

# update_order()

chai = "plain"

def front_desk():
    def kitchen():
        global chai
        chai = "Irani"
    kitchen()


front_desk()
print("global chai is ", chai)