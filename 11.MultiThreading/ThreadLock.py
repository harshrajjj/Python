import threading


counter =0

lock = threading.Lock()

def increment():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
        # counter += 1

thread = [threading.Thread(target=increment) for _ in range(5)]

[t.start() for t in thread]
[t.join() for t in thread]

print(f"Final counter value: {counter}")