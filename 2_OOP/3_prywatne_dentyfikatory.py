class Pracownik:
    def __init__(self, pozycja, pesel):
        self.pozycja = pozycja
        self.__pesel = pesel

    def __str__(self):
        return f'{self.pozycja}, {self.__pesel}'

worker1 = Pracownik("engineer", '1234')
print(worker1)
worker1.__pesel = '6789'
print(worker1)
print(worker1.__pesel)

