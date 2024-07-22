class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.__wiek = wiek

    def __str__(self):
        return f'{self.imie},  {self.__wiek}'

    def ustaw_wiek(self, wiek):
        if wiek > 0:
            self.__wiek = wiek
        else:
            raise ValueError('Wiek musi być dodatni')

    def pobierz_wiek(self):
        return f'Wiek to {int(self.__wiek/10)}0 kilka lat'

osoba = Osoba('Kamil', 35)
print(osoba.imie)
# print(osoba.__wiek)

print(osoba.pobierz_wiek())
osoba.ustaw_wiek(23)
print(osoba.pobierz_wiek())
osoba.ustaw_wiek(-23)

