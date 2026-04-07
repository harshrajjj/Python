def local_chai():
    yield "malsala chai"
    yield "ginger chai"


def important_chai():
    yield "macha"
    yield "woolang"

def full_chai():
    yield from local_chai()
    yield from important_chai()

for chai in full_chai():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "waiting for order"
    except:
        print("stall is closed")


stall = chai_stall()
print(next(stall))#start the generator
stall.close()#close the generator