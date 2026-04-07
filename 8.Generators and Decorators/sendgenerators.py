def chai_customer():
    print("welcome to the chai shop")
    order  = yield
    while True :
        print(f"here is your " + order)
        order = yield

stall = chai_customer()

next(stall)#start the generator
stall.send("chai")#send the order to the generator
stall.send("chai with ginger")

