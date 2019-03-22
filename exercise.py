import requests
import json
from random import choice

json_response_countries = requests.get('https://raw.githubusercontent.com/everypolitician/everypolitician-data/master/countries.json')
list_of_countries = json.loads(json_response_countries.content)

random_country = choice(list_of_countries)

print(f"Selected country: {random_country['name']}")

print()
print(f"Legislatures of {random_country['name']}:")
for l in random_country["legislatures"]:
    print(l["name"])

random_legislature = choice(random_country["legislatures"])
legislature_info_url = random_legislature["popolo_url"]

json_response_politicinas = requests.get(legislature_info_url)
politicians_dict = json.loads(json_response_politicinas.content)

list_of_politicians = politicians_dict["persons"]

random_politician = choice(list_of_politicians)
politician_info = f"Name: {random_politician['name']}"

print()
print("Randomly selected politician:")
print(politician_info)
