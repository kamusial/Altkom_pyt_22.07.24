import multiprocessing
import time

def square(n):
    print(f'Proces {multiprocessing.current_process().name}: liczy pole z {n}')
    time.sleep(1)
    return n * n

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    with multiprocessing.Pool(processes=3) as pool:
        result = pool.map(square, numbers)

    print(f'Result: {result}')