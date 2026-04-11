import threading 
import time

def cpu_heavy():
    print("Starting CPU heavy task")
    count = 0
    for i in range(10**7):
        count += 1
    print("Finished CPU heavy task")

start = time.time()
t1 = [threading.Thread(target=cpu_heavy) for _ in range(4)]
[t.start() for t in t1]
[t.join() for t in t1]
end = time.time()
print(f"Total time taken: {end - start:.2f} seconds")

print("All threads finished")