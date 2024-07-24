import re

text = "This is the first line.\nAnd this is the second line."
pattern = r'This.*line.'
match = re.search(pattern, text)
print(match.group())

match = re.search(pattern, text, re.DOTALL)
print(match.group())

text = "First line\nSecond line\nThird line"
pattern = r'^Second'
match = re.search(pattern, text, re.MULTILINE)
print(match.group())

