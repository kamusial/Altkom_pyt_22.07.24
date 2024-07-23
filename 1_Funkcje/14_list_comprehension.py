liczby = [1, 2, 3, 4, 5]
kwadraty = [x ** 2 for x in liczby]
print(kwadraty)

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parzyste = [x for x in liczby if x % 2 == 0]
print(parzyste)

slowa = ['jablko', 'banan', 'piesek', 'kot']
dlugosci = [len(slowo) for slowo in slowa]
# dlugosci = []
# for slowo in slowa:
#     dlugosci.append(len(slowo))
print(dlugosci)


# zagniezdzona
lista_list = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
splaszczona = [element for podlista in lista_list for element in podlista]
print(splaszczona)

# warunkowe
liczby = [1, 2, 3, 4, 5]
opis = ['mala' if x <= 3 else 'duza' for x in liczby]
print(opis)
