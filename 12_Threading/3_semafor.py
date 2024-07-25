import threading
import time
import random

def worker(semaphore, worker_id):
    print(f'Worker {worker_id} czeka na dostęp do semaforu')
    with semaphore:
        print(f'Worker {worker_id} zajął semafor')
        work_time = random.uniform(0.5, 2.0)
        time.sleep(work_time)
        print(f'Worker {worker_id} zwalnia semafor po {work_time}s')
    print(f'Worker {worker_id} zwolnił semafor')

semaphore = threading.Semaphore(2)

threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(semaphore, i))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print('Wszystko zakonczone')