# funkcja map
# podniesć każdy element listy do kwadratu

liczby = [1, 2, 3, 4, 5]
kwadraty = list(map(lambda x: x ** 2, liczby))
print(kwadraty)  # Wynik: [1, 4, 9, 16, 25]