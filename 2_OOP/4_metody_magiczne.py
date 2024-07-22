class Auto:
    def __init__(self, marka, rocznik, kondycja):
        self.marka = marka
        self.rocznik = rocznik
        self.kondycja = kondycja

    def __str__(self):
        return f'{self.marka}'

    def __eq__(self, other):
        if self.rocznik <= other.rocznik + 1 and self.rocznik >= other.rocznik - 1:
            return self.kondycja == other.kondycja
        return False

#    def __add__(self, other):   # dodawanie
#    def __sub__(self, other):   # odejmowanie
#    def __mul__(self, other):   # mnozenie
#    def __len__(self):          # dlugosc

auto1 = Auto('Toyota', 1998, 4)
auto2 = Auto('BMW', 1999, 4)

print(auto1 == auto2)

