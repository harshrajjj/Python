from multiprocessing import Process, Queue

def prepare_cahi(queue):
    queue.put("masala chai is ready")


if __name__ == "__main__":
    q = Queue()
    p = Process(target=prepare_cahi, args=(q,))
    p.start()
    p.join()
    print(q.get())
