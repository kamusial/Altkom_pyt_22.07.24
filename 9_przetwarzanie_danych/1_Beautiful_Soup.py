from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki'
r = requests.get(url)
html_content = r.text

soup = BeautifulSoup(html_content, 'html.parser')
print(soup.prettify())
h1_tag = soup.find('h1')
print(h1_tag.text)

elements = soup.find_all(class_='example_class')
for element in elements:
    print(element.text)

# nawigacja
# znajdź rodzica elementu
parent = h1_tag.parent

# znajdź dzieci elementu
for child in parent.children:
    print(child.name)

# znajdź rodzeństwo
next_sibling = h1_tag.next_sibling
print(next_sibling)