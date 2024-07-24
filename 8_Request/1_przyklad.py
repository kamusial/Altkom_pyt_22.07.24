import requests

response = requests.get('https://simple-books-api.glitch.me/status')
print(response.status_code)
print(response.text)


page = 'https://simple-books-api.glitch.me/orders'
data = {
  "bookId": 1,
  "customerName": "John"
}
response = requests.post(page, json=data)
print(response.status_code)
print(response.json())


authorization_page = 'https://simple-books-api.glitch.me/api-clients/'
authorization_data = {
   "clientName": "Kamil",
   "clientEmail": "qvalentin@example.com"
}
response = requests.post(authorization_page, json=authorization_data)
print(response.status_code)
print(response.json())