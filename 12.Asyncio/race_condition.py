import threading


chai_stock = 0

def buy_chai():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1


thread =[threading.Thread(target=buy_chai) for _ in range(2)]

for t in thread:
    t.start()

for t in thread:
    t.join()    

print(chai_stock)