class Osoba:
    def __init__(self, imie, wiek):
        self._imie = imie
        self._wiek = wiek

    def getImie(self):
        return self._imie

    def setImie(self, value):
        if not value:
            raise ValueError("Imie nie moze byc puste")
        self._imie = value

    def getWiek(self):
        return self._wiek

    def setWiek(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Wiek musi byc dodatnią liczbą całkowitą")
        self._wiek = value

osoba = Osoba('Kamil', 36)
print(osoba.getImie())
print(osoba.getWiek())
osoba.setImie('Ela')
osoba.setWiek(25)
print(osoba.getImie())
print(osoba.getWiek())






