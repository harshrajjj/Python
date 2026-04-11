import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def thread1():
    with lock_a:
        print("Thread 1: Acquired lock A")
        with lock_b:
            print("Thread 1: Acquired lock B")

def thread2():
    with lock_b:
        print("Thread 2: Acquired lock B")
        with lock_a:
            print("Thread 2: Acquired lock A")


t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)


t1.start()
t2.start()
t1.join()
t2.join()
print("Both threads completed")

#python profiling tools:
#py-spy, cProfile, line_profiler, memory_profiler, pyinstrument, snakeviz, vprof, pyflame, yappi, pycallgraph, pyprof2calltree, py-spy, cProfile, line_profiler, memory_profiler, pyinstrument, snakeviz, vprof, pyflame, yappi, pycallgraph, pyprof2calltree