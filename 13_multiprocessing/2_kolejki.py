import multiprocessing
import time
import random

def producer(queue, n_items):
    for _ in range(n_items):
        item = random.randint(1, 100)
        print(f"Producing {item}")
        queue.put(item)
        time.sleep(random.uniform(0.1, 0.5))
    queue.put(None)  # Wstawienie znacznika końca pracy

def consumer(queue):
    while True:
        item = queue.get()
        if item is None:  # Sprawdzenie znacznika końca pracy
            break
        print(f"Consuming {item}")
        time.sleep(random.uniform(0.1, 0.5))

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    n_items = 10

    producer_process = multiprocessing.Process(target=producer, args=(queue, n_items))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("All items have been produced and consumed.")
