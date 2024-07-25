import threading

lock = threading.Lock()
def thread_task():
    with lock:
        # sekcja krytyczne
        pass


rlock = threading.RLock()
    with rlock:
        pass