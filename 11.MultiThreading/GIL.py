# import threading
# import time

# def brew_coffee(name):
#     print(f"{threading.current_thread().name} is brewing {name} coffee...")
#     count =0
#     for _  in range(100_000_000):
#         count += 1
#     print(f"{threading.current_thread().name} has finished brewing {name} coffee.")
    

# t1 = threading.Thread(target=brew_coffee, args=("Espresso",), name="Thread-1")
# t2 = threading.Thread(target=brew_coffee, args=("Latte",), name="Thread-2")

# start = time.time()

# t1.start()
# t2.start()

# t1.join()
# t2.join()
# end = time.time()
# print(f"Total time taken: {end - start:.2f} seconds")

# print("All threads finished")


from multiprocessing import Process
import time

def brew_coffee():
    print(f"starting to brew coffee...")
    count =0
    for _  in range(100_000_000):
        count += 1
    print(f"finished brewing coffee.")


if __name__ == "__main__":
    p1 = Process(target=brew_coffee, args=("Espresso",))
    p2 = Process(target=brew_coffee, args=("Latte",))

    start = time.time()

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")

    print("All processes finished")