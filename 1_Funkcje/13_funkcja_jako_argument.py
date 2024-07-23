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

def jest_ponizej_30(osoba):
    return osoba['wiek'] > 30


# Operacje
def pobierz_imie(osoba):
    return osoba['imie']

def opis(osoba):
    return f'{osoba['imie']} ma {osoba['wiek']} lat i jest {osoba['zawod']}.'


inzynierowie = filtruj_osoby(osoby, jest_inz)
print(f'Inzynierowie: {przetworz_osoby(inzynierowie, opis)}')

mlodsze = filtruj_osoby(osoby, jest_ponizej_30)
print(f'osoby mlodsze niz 30 lat: {przetworz_osoby(mlodsze, pobierz_imie)}')

