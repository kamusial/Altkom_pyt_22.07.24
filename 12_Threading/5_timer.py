import threading

def delayed_function():
    print('Funkcja uruchomiona po 3 sekundach')

timer = threading.Timer(3, delayed_function)
timer.start()
