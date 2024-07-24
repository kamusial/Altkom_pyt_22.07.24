from bs4 import BeautifulSoup
import requests

# Pobieranie strony internetowej
url = 'https://example.com'
response = requests.get(url)
html_content = response.text

# Parsowanie HTML
soup = BeautifulSoup(html_content, 'html.parser')

# Znajdowanie wszystkich linków
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    text = link.text
    print(f'{text}: {href}')
