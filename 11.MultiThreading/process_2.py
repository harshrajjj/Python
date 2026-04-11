from multiprocessing import Process 
import time

def cpu_heavy():
    print("Starting CPU heavy task")
    count = 0
    for i in range(10**7):
        count += 1
    print("Finished CPU heavy task")

if __name__ == "__main__":
    start = time.time()
    p1 = [Process(target=cpu_heavy) for _ in range(4)]
    [t.start() for t in p1]
    [t.join() for t in p1]
    end = time.time()
    print(f"Total time taken: {end - start:.2f} seconds")

    print("All threads finished")