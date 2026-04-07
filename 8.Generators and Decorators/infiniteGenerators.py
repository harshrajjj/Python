def infinite_chai():
    count = 1
    while True:
        yield "cup " + str(count)
        count += 1


refill = infinite_chai()

for  _ in range(5):
    print(next(refill))

    