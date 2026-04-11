import threading    
import time

def monitor_tea_temperature():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)       

t = threading.Thread(target=monitor_tea_temperature).start()

print("Main thread is doing other work...")

#profiling
# py -m cProfile -s time nondeamon.py  