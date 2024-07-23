import itertools

# Nieskończony licznik zaczynający od 10
for i in itertools.count(10):
    if i > 20:  # zakończenie pętli, by uniknąć nieskończonej pętli
        break
    print(i)

# Powtarza elementy listy nieskończenie wiele razy
licznik = 0
for item in itertools.cycle(['A', 'B', 'C']):
    if licznik > 7:
        break
    print(item)
    licznik += 1

# Generuje wszystkie możliwe permutacje
for p in itertools.permutations([1, 2, 3]):
    print(p)

# Generuje kombinacje dwuelementowe z listy
for c in itertools.combinations([1, 2, 3, 4], 2):
    print(c)

for c in itertools.combinations_with_replacement([1, 2, 3, 4], 2):
    print(c)

# Łączy listy w jedną sekwencję
for item in itertools.chain([1, 2, 3], ['A', 'B', 'C']):
    print(item)


# Łączy listy w jedną sekwencję
print(list(itertools.chain.from_iterable(['1', '2', ['3', '4', '5'], ['A', 'B', 'C']])))

# Grupuje elementy według długości
data = ['abc', 'de', 'fgh', 'i', 'jk']
for k, g in itertools.groupby(data, key=len):
    print(f'Klucz: {k}, Grupa: {list(g)}')

