class BMW:

    bagaznik = []
    def __init__(self, kolor: str = 'czarne', kondycja: int = 1, rocznik: int = 1900):
        self.kolor = kolor
        self.__ilosc_paliwa = 10
        self.kondycja = kondycja
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14
        self.wiek = 2024 - rocznik

    def __str__(self):
        return f'Auto ma kolor {self.kolor} i ma {self.__ilosc_paliwa} litrow paliwa'

    def zasieg(self):
        zasieg = self.__ilosc_paliwa / self.spalanie_na_100 * 100 * 0.9
        return round(zasieg)


    def ustaw_tryb(self, tryb):
        if tryb == 'eco':
            self.spalanie_na_100 = 10
            self.tryb_ekonomiczny = True
            print('Tryb eco')
        elif tryb == 'normal':
            self.spalanie_na_100 = 14
            self.tryb_ekonomiczny = False
            print('Tryb normal')
        else:
            print('tryb nierozpoznany, brak zmian')


    def tryb_eco(self):
        self.tryb_ekonomiczny = True
        self.spalanie_na_100 = 11


    def tryb_normal(self):
        self.tryb_ekonomiczny = False
        self.spalanie_na_100 = 14


    def odejmij_paliwo(self, ile):
        if self.__ilosc_paliwa <= ile:
            print('Brak paliwa')
        else:
            self.__ilosc_paliwa -= ile


moje_auto = BMW('zielone', 4, 1987)
print(moje_auto.kolor)
moje_auto.odejmij_paliwo(3)
moje_auto.odejmij_paliwo(8)
print(moje_auto.spalanie_na_100)
moje_auto.tryb_eco()
print(moje_auto.spalanie_na_100)
print(moje_auto)
print(moje_auto.zasieg())

