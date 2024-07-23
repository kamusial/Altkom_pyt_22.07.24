osoby = [
    {"imie": "Anna", "wiek": 30, "zawod": "Inżynier"},
    {"imie": "Jan", "wiek": 40, "zawod": "Artysta"},
    {"imie": "Kasia", "wiek": 22, "zawod": "Programista"},
    {"imie": "Stefan", "wiek": 35, "zawod": "Inżynier"},
    {"imie": "Ewa", "wiek": 28, "zawod": "Architekt"}
]

def filtruj_osoby(osoby, kryterium):
    return [osoba for osoba in osoby if kryterium(osoba)]

def przetworz_osoby(osoby, operacja):
    return [operacja(osoba) for osoba in osoby]


# filtrowanie
def jest_inz(osoba):
    return osoba['zawod'] == 'Inżynier'

# Operacje
def pobierz_imie(osoba):
    return osoba['imie']



