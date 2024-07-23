def dekorator_logujacy(func):
    def wrapper(*args, **kwargs):
        print(f'Wywolanie funkcji')
        result = func(*args, **kwargs)
        print(f'zakonczenie funkcji')
        return result
    return wrapper


def dekorator_zabezpieczajacy(func):
    def wrapper(dzielna, dzielnik):
        print('sprawdzam parametry)')
        if dzielnik == 0:
#            print(f'Blad, dzielenie przez zero')
            raise ValueError('Blad, dzielenie przez 0')
        return func(dzielna, dzielnik)
    return wrapper

@dekorator_logujacy
@dekorator_zabezpieczajacy
def dzielenie(a, b):
    return a / b


@dekorator_logujacy
def dodaj(a, b):
    return a + b

print(dodaj(3, 5))

try:
    print(dzielenie(3, 0))
except ValueError as e:
    print(e)
