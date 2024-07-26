import multiprocessing
import time

def deamon_task():
    name = multiprocessing.current_process().name
    print(f'Process {name} rozpoczęty')
    time.sleep(5)
    print(f'Process {name} zakończony')

def nondeamon_task():
    name = multiprocessing.current_process().name
    print(f'Process {name} rozpoczęty')
    time.sleep(2)
    print(f'Process {name} zakończony')

if __name__ == '__main__':
    deamon_process = multiprocessing.Process(target=deamon_task, name='Deamon Process')
    deamon_process.deamon = True

    non_deamon_process = multiprocessing.Process(target=nondeamon_task, name='non_deamon Process')
    non_deamon_process.deamon = False

    deamon_process.start()
    non_deamon_process.start()

    non_deamon_process.join()

    print(f'Koniec')
