def funkcja_args(imie, pesel, *kary):
    suma = 0
    for kara in kary:
        suma += kara
    print(f' Kierowca {imie} o nr pesel {pesel}\nsuma kar: {suma}')
    if suma > 1000:
        print('prawo jazdy zabrane')
    elif suma > 800:
        print('zaraz zabiorą prawko jazdy')

funkcja_args('Kamil', '54353', 50, 32, 343, 111, 200, 211)


