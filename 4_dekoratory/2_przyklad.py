import functools
import time

def zaawansowany_dekorator(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # tworzenie klucza cache na podstawie argumentów funkcji
        cache_key = args + tuple(kwargs.items())

        # Logowanie
        print(f'Funkcja {func.__name__} z {args} i {kwargs}')

        # sprawdzanie, czy wynik jest w cache
        if cache_key in cache:
            print(f'Uzywam wartosci z cache')
            return cache[cache_key]

        # pomiar czasu
#        start_time = time.time()
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
#        end_time = time.time()
        duration = end_time - start_time
        print(f'{func.__name__}, czas trwania {duration:.4f}s')

        # zapisanie wyniku w cache
        cache[cache_key] = result
        return result
    return wrapper

@zaawansowany_dekorator
def dluga_operacja(x, y):
    time.sleep(1)
    return x * y + x / y


print(dluga_operacja(1, 2))
print(dluga_operacja(1, 2))
print(dluga_operacja(5, 4))