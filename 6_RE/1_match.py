import re

pattern = r'a'
text = 'abc'
match = re.match(pattern, text)
print(match.group())

pattern = r'a.b'
text = 'acb'
match = re.match(pattern, text)
print(match.group())

pattern = r'ab*c'    #  * zero lub więcej
text = r'abbbbc'
match = re.match(pattern, text)
print(match.group())

pattern = r'^abc$'
text = r'abc'
match = re.match(pattern, text)
print(match.group())

pattern = r'ab?c'     #  ? zero lub jedno
text = r'abbbc'
match = re.match(pattern, text)
if match:
    print(match.group())
else:
    print('brak dopasownaia')

pattern = r'ab+c'     #  + jedno lub więcej
text = r'ac'
match = re.match(pattern, text)
if match:
    print(match.group())
else:
    print('brak dopasownaia')

pattern = r'[abc]'     #  + jedno lub więcej
text = r'a'
match = re.match(pattern, text)
if match:
    print(match.group())
else:
    print('brak dopasownaia')
