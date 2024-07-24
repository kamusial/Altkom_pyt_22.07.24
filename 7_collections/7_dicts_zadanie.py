from collections import defaultdict, OrderedDict

# struktura do przechowywania projektów
projects = OrderedDict()

def create_task_structure():
    return defaultdict(list)


def add_project(project_name):
    if project_name not in projects:
        projects[project_name] = create_task_structure()
    else:
        print(f'projekt {project_name} istnieje')


def add_task(project_name, task, status='do zrobienia'):
    if project_name in projects:
        projects[project_name][status].append(task)
    else:
        print(f'projekt {project_name} nie istnieje')


def change_task_status(project_name, task, new_status):
    if project_name in projects:
        for status, tasks in projects[project_name].items():
            if task in task:
                tasks.remove(task)
                projects[project_name][new_status].append(task)
                return
        print(f'Zadanie {task} nie znaleziono w projekcie')
    else:
        print(f'projekt {project_name} nie istnieje')


def display_tasks(project_name):
        if project_name in projects:
            print(f'Zadania w projekcie {project_name}:')
            for status, tasks in projects[project_name].items():
                print(f'Status: {status}')
                for task in tasks:
                    print(f'   - {task}')
        else:
            print(f'projekt {project_name} nie istnieje')

add_project('Projekt A')
add_project('Projekt B')
add_task('Projekt A', 'Zadanie 1')
add_task('Projekt A', 'Zadanie 2', status='w trakcie')
add_task('Projekt B', 'Zadanie 3', status='do zrobienia')

display_tasks('Projekt A')
display_tasks('Projekt B')

change_task_status('Projekt A', 'Zadanie 1', 'w trakcie')
change_task_status('Projekt B','Zadanie 3', 'zrobione')

display_tasks('Projekt A')
display_tasks('Projekt B')