import re

# search - szuka w całym stringu
pattern = r'abc'
text = 'xyzabcdef'
match = re.search(pattern, text)
if match:
    print(match.group())  # Wynik: abc


pattern = r'ab+c'     #  + jedno lub więcej
text = r'Kamil i PythonabbbbcPythonabc'
match = re.search(pattern, text)
if match:
    print(match.group())
else:
    print('brak dopasownaia')




