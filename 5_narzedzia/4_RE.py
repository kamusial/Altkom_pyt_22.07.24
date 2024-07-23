import re

text = 'kamil i pies i kamil i pies i pies i pies'
matches = re.findall('pies', text)
print(matches)

text_zmieniony = re.sub('pies', 'kot', text)
print(text_zmieniony)

text= 'strona internetowa http://example.com end'
matches = re.findall(r'http://[a-zA-Z0-9./]+', text)
print(matches)
