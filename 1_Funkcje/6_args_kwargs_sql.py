def stworz_zapytanie_sql(tabela: str, *kolumny: str, **warunki) -> str:

    # SELECT
    if kolumny:
        kolumny_sql = ', '.join(kolumny)
    else:
        kolumny_sql = '*'

    # WHERE
    warunki_sql = ' AND '.join([f"{klucz}='{wartosc}'" for klucz, wartosc in warunki.items()])

    # Pełne zapytanie
    if warunki_sql:
        zapytanie = f'SELECT {kolumny_sql} FROM {tabela} WHERE {warunki_sql};'
    else:
        zapytanie = f'SELECT {kolumny_sql} FROM {tabela};'

    return zapytanie


zapytanie1 = stworz_zapytanie_sql("uzytkownicy", "imie", "nazwisko", wiek=30)
print(zapytanie1)

zapytanie2 = stworz_zapytanie_sql("produkty", "nazwa", "cena", kategoria="biznes", kolor='czerwony')
print(zapytanie2)