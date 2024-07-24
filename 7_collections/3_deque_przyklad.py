from collections import deque

# kolejki dla różnych priorytetów
high_priority = deque()
medium_priority = deque()
low_priority = deque()

def add_task(task, priority='medium'):
    if priority == 'high':
        high_priority.append(task)
    elif priority == 'medium':
        medium_priority.append(task)
    elif priority == 'low':
        low_priority.append(task)
    else:
        raise ValueError('Nieznany proprytet: {}'.format(priority))

def process_task():
    if high_priority:
        task = high_priority.popleft()
        print(f'Przetwarzam zadanie o wysokim prio: {task}')
    elif medium_priority:
        task = medium_priority.popleft()
        print(f'Przetwarzam zadanie o srednim prio: {task}')
    elif low_priority:
        task = low_priority.popleft()
        print(f'Przetwarzam zadanie o niskim prio: {task}')
    else:
        print('Nie przetwarzam - brak zadan')

def display_queues():
    print(f'Zadania o wysokim prio: {list(high_priority)}')
    print(f'Zadania o srednim prio: {list(medium_priority)}')
    print(f'Zadania o niski prio: {list(low_priority)}')


add_task('Zadanie 1', 'high')
add_task('Zadanie 2')
add_task('Zadanie 3')
add_task('Zadanie 4', 'low')
add_task('Zadanie 5', 'high')

display_queues()

process_task()
process_task()
process_task()

display_queues()