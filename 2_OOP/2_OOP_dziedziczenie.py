class Pojazd:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.wiek = 2024 - rok

    def __str__(self):
        return f'Pojazd to: {self.marka} {self.model}'

    def uruchom_silnik(self):
        return f'silnik w {self.model} uruchomiony'


class Samochod(Pojazd):
    def __init__(self, marka, model, rok, ilosc_drzwi):
        super().__init__(marka, model, rok)
        self.ilosc_drzwi = ilosc_drzwi

    def __str__(self):
        return f'Samochod to: {self.marka} {self.model}'

    def wlacz_klimatyzacje(self):
        return "klima wlaczona"


class Motocykl(Pojazd):
    def __init__(self, marka, model, rok, typ):
        super().__init__(marka, model, rok)
        self.typ = typ

    def __str__(self):
        return f'Motor to: {self.typ}'

    def trik(self):
        return f'trik w {self.typ}'



moj_pojazd = Pojazd('Toyota', 'Corolla', 2021)
print(moj_pojazd)
print(moj_pojazd.uruchom_silnik())

moje_auto = Samochod('Toyota', 'Yaris', 2011, 5)
print(moje_auto)
print(moje_auto.uruchom_silnik())
print(moje_auto.wlacz_klimatyzacje())

