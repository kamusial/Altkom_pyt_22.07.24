from functions import mnozenie
import pytest

def test_basic():
    assert mnozenie(2, 3) == 6
    assert mnozenie(3, 2) == 6
    assert mnozenie(1, 5) == 5
    assert mnozenie(0, 4) == 0
    assert mnozenie(-3, 5) == -15

def test_advanced():
    assert mnozenie(1.1, 10) == 11
    assert mnozenie(1.1, 100) == 110
    assert mnozenie(0.000001, 0.001) == 0.000000001
    assert mnozenie('mama', 5) == None
