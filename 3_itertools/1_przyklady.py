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

