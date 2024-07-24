import requests

response = requests.get('https://simple-books-api.glitch.me/status')
print(response.status_code)
print(response.text)

# authorization_page = 'https://simple-books-api.glitch.me/api-clients/'
# authorization_data = {
#    "clientName": "Kamil",
#    "clientEmail": "qsavaddfddlentin@example.com"
# }
# response = requests.post(authorization_page, json=authorization_data)
# print(response.status_code)
# print(response.json())

token = '737017e94fa29d4f0da8c2650ca9795f80078b600bd80bd9d223a0e63200c12b'
page = 'https://simple-books-api.glitch.me/orders'

data1 = {
  "bookId": 1,
  "customerName": "John"
}
data2 = {
  "bookId": 2,
  "customerName": "John"
}
response1 = requests.post(page, json=data1, headers={'Authorization': token})
response2 = requests.post(page, json=data2, headers={'Authorization': token})
print(response1.status_code)
print(response1.json())
print(response2.status_code)
print(response2.json())

response3 = requests.get(page, headers={'Authorization': token})
print(response3.status_code)
print(response3.json())


