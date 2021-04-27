import json
import pandas as pd
with open("50_features.json") as file:
    data = json.load(file)
nuts1 = ["UKC", "UKD", "UKE", "UKF", "UKG", "UKH", "UKI", "UKJ", "UKK"]

out = {}

for item in data:
    out[item]={key: 0 for key in nuts1}

df = pd.DataFrame.from_dict(out)

df.loc["UKD", "tower"]+=1

print(df)
