# json

import json

data = {
    "name": "John",
    "age": 30,
    "is_student": False,
    "courses": ["Math", "Science"],
    "address": {
        "city": "New York",
        "zip": "10001"
    }
}

# konwersja na JSON
json_string = json.dumps(data, indent=4, separators=(',',': '))
print(json_string)

python_file = json.loads(json_string)
print(python_file)


# YAML
import yaml
with open('4_yaml.yml', 'r') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
print(data)




