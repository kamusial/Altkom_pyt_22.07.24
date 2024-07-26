def mnozenie(a, b):
    if isinstance(a, str) or isinstance(b, str):
        return None
    return round(a * b, 10)