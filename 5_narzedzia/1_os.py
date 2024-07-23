import os

print(os.getcwd())
new_dir = "C:\\Users\\Trener19\\"
os.chdir(new_dir)
print(f'zmieniono katalog roboczy na: {os.getcwd()}')

path = '.'
files_and_directories = os.listdir(path)
print(f'zawartosc katalogu {path}: {files_and_directories}')

os.mkdir('new_directory')
print('Katalog "new_directory" utworzony')
os.rename('new_directory', 'DIRRR')
os.rmdir('DIRRR')
print('usunieto')

# ustawienie zmiennej srodowiskowej
os.environ['NEW_ENV_PATH'] = '1234'
path_var = os.environ.get('NEW_ENV_PATH')
print(f'path_var: {path_var}')
