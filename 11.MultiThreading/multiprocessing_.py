from multiprocessing import Process
import time

def brew_coffee(name):
    print("Brewing coffee for ", name)
    time.sleep(2)
    print("Coffee is ready for ", name)

if __name__ == "__main__":
    chai_maker = [
        Process(target=brew_coffee, args=(f"Customer {i}",)) for i in range(5)
    ]

    #starting processes
    for maker in chai_maker:
        maker.start()

    #waiting for processes to finish
    for maker in chai_maker:
        maker.join()

    print("All processes finished")