import requests

data = {'key1': 'value1', 'key2': 'value2'}
response = requests.put('https://httpbin.org/put', data=data)
print(response.status_code)
print(response.json())


response = requests.delete('https://httpbin.org/delete')
print(response.status_code)
print(response.json())


response = requests.head('https://api.github.com')
print(response.status_code)
print(response.headers)


data = {'key1': 'new_value'}
response = requests.patch('https://httpbin.org/patch', data=data)
print(response.status_code)
print(response.json())




