def funkcja_demo(*args, **kwargs):
    # Wyświetlanie argumentów pozycyjnych
    print("Argumenty pozycyjne (*args):")
    for arg in args:
        print(arg)

    # Wyświetlanie argumentów nazwanych
    print("\nArgumenty nazwane (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Wywołanie funkcji z różnymi argumentami
funkcja_demo(1, 2, 3, imie="Jan", wiek=30, miasto="Wrocław")
funkcja_demo("jabłko", "banan", kolor="czerwony", smak="słodki")
