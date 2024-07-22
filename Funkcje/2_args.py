def dodawanie_args(*liczby):
    suma = 0
    for liczba in liczby:
        suma += liczba
    return suma

def dodawanie_no_args(liczby: list):
    suma = 0
    for liczba in liczby:
        suma += liczba
    return suma


print(dodawanie_args(1, 4, 4, 3, 2, 2))
print(dodawanie_no_args([1, 4, 4, 3, 2, 2]))