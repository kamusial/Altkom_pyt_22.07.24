def mnozenie(a, b=3, c=4):
    wynik = a * b * c
    return wynik

def pokaz_3ci_element(nazwa: str) -> str:
    return nazwa[2]


print('Siema')
print(mnozenie(1, 2))

print(pokaz_3ci_element('Mama'))
moja_lista = [1, 2, 3, 5, 4, 3]
print(pokaz_3ci_element(moja_lista))
# print(pokaz_3ci_element(3.542))


