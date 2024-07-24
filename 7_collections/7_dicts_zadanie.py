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
