from multiprocessing import Process
from threading import Thread
import time


def print_numbers(name):
    for i in range(10):
        print(f"{name}\t{i}")
        time.sleep(1)

threads = []
for i in range(3):
    thread = Thread(target=print_numbers, args=(f"Thread-{i}",), daemon=True)
    threads.append(thread)
    thread.start()

# run the code with and without joins, see the difference
for thread in threads:
    thread.join()


if __name__ == "__main__":
    processes = []

    for i in range(3):
        process = Process(target=print_numbers, args=(f"Process-{i}",))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
