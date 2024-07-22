def przywitanie_funkcja(**dane):
    for key, value in dane.items():
        print(f'{key}: {value}')
    print(f'Hej {dane['imie']}')
    if dane['pesel'] is not None:
        print('pesel zweryfikowany')
    print(f'traviasz do zespolu {dane['zespol']}')


przywitanie_funkcja(imie='Kamil', pesel=987398, wiek=36, zespol='ADR36')
