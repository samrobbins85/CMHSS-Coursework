import json
with open("all_features.json") as file:
    data = json.load(file)
print(list(data))

with open("50_features.json", "w") as out_file:
    json.dump(list(data)[0:50],out_file)