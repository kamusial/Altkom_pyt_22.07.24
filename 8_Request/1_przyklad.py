import requests

response = requests.get('https://simple-books-api.glitch.me/status')
print(response.status_code)
print(response.text)

authorization_page = 'https://simple-books-api.glitch.me/api-clients/'
authorization_data = {
   "clientName": "Kamil",
   "clientEmail": "qsavaddfddlentin@example.com"
}
response = requests.post(authorization_page, json=authorization_data)
print(response.status_code)
print(response.json())

token = response.json()['accessToken']
page = 'https://simple-books-api.glitch.me/orders'
data = {
  "bookId": 1,
  "customerName": "John"
}

response = requests.post(page, json=data, headers={'Authorization': token})

print(response.status_code)
print(response.json())


