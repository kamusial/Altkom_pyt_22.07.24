liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

parzyste_liczby = list(filter(lambda x: x % 2 == 0, liczby))

print(parzyste_liczby)