import sys
print(f'Python version: {sys.version}')
print(f'Python version: {sys.version_info}')

print('Aktualna sciezka poszukiwnaia modulow')
print(sys.path)
# dodanie nowej
sys.path.append('/Users/Trener19/Desktop')

print('Argumenty przekazane do skryptu:')
print(sys.argv)

# przekierowanie stdout do pliku
with open('output.txt', 'w') as f:
    sys.stdout = f
#przywrocenie
sys.stdout = sys.__stdout__

sys.exit(1)
