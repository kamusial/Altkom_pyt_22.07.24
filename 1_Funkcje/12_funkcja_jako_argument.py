def kwadrat (x):
    return x * x

def podwoj(x):
    return x * 2

def zastosuj(lista, funkcja):
    return [funkcja(x) for x in lista]


liczby = [1, 2, 3, 4, 5]
kwadraty = zastosuj(liczby, kwadrat)
print(f'kwadraty listy: {kwadraty}')

podwojone = zastosuj(liczby, podwoj)
print(f'podwojone liczby: {podwojone}')