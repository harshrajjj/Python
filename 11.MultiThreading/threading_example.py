import threading 
import time

def take_orders():
    for i in range(5):
        print("Taking order ", i)
        time.sleep(1)   

def prepare_food():
    for i in range(5):
        print("Preparing food ", i)
        time.sleep(2)

#creating threads
t1 = threading.Thread(target=take_orders)
t2 = threading.Thread(target=prepare_food)

#starting threads
t1.start()
t2.start()

#waiting for threads to finish
t1.join()
t2.join()

print("All threads finished")