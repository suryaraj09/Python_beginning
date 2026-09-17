import json

# people_string = '''{
#   "People": [
#     {
#       'name": "John",
#       "age": 30,
#       "city": "New York"
#     },
#     {
#       'name": "Surya",
#       "age": 21,
#       "city": "Ahmedabad"
#     },
#     {
#       'name": "Raj",
#       "age": 25,
#       "city": "New York"
#     }
#   ]
# }'''

# data = json.loads(people_string)

# # Access the list under the "People" key
# for person in data['People']:
#     del person['city']

# new_string = (json.dumps(data, indent=2))
# print(new_string)

with open('states.json', 'r') as f:
    data = json.load(f)

for states in data['states']:
    del states['area_codes']
    print(f"{states['name']} --> {states['abbreviation']}")


with open('new_states.json', 'w') as f:
    json.dump(data, f, indent = 2)