import threading
import time

def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


# Tworzenie wątku
thread1 = threading.Thread(target=print_numbers)

# Uruchamianie wątku
thread1.start()

# Kontynuacja głównego wątku
for i in range(5, 10):
    print(i)
    time.sleep(1)

# oczekiwanie za zakończenie wątku
thread1.join()
