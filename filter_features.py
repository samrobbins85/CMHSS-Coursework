import json
with open("improved_all_features.json") as file:
    data = json.load(file)

data = {k: v for k, v in data.items() if v > 5}
print(list(data))

with open("improved_features_gt_5.json", "w") as out_file:
    json.dump(list(data),out_file)