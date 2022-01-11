import json

data = {
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}

json_dumps = json.dumps(data)
print(json_dumps)
# with open('data_file.json', 'w') as f:
#     f.write(json_dumps)
with open('data_file.json', 'w') as f:
    json.dump(data, f)