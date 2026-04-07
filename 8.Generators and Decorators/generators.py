def serve_chai():
    yield "Boil water"
    yield "Add tea leaves"
    yield "Add milk"

stall  = serve_chai()

for cup in stall:
    print(cup)


def get_chai_list():
    return ["Boil water", "Add tea leaves", "Add milk"]

def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = get_chai_gen()

print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai))