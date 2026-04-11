# import threading
# import time

# def boil_milk():
#     print("Boiling milk...")
#     time.sleep(2)
#     print("Milk is boiled.")


# def toast_bread():
#     print("Toasting bread...")
#     time.sleep(3)
#     print("Bread is toasted.")


# start = time.time()
# t1 = threading.Thread(target=boil_milk)
# t2 = threading.Thread(target=toast_bread)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end = time.time()
# print(f"Total time taken: {end - start:.2f} seconds")

# print("All threads finished")



import threading
import time

def prepare_chai(type,wait_time):
    print(f"Preparing chai...{type}")
    time.sleep(wait_time)
    print(f"Chai is ready.{type}")

t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))

start = time.time()
t1.start()
t2.start()

t1.join()
t2.join()
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")

print("All threads finished")