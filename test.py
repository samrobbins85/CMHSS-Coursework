import json
import pandas as pd
with open("50_features.json") as file:
    data = json.load(file)
nuts1 = ["UKC", "UKD", "UKE", "UKF", "UKG", "UKH", "UKI", "UKJ", "UKK"]

out = {}

for item in data:
    out[item]={key: 0.0 for key in nuts1}

df = pd.DataFrame.from_dict(out)

area_count = {key:2 for key in nuts1}

area_count["UKJ"]=4

df.loc["UKD", "tower"]+=1

df.loc["UKJ", "tower"]+=1


df2=pd.DataFrame(area_count, index=[0])


print(df.div(df2.iloc[0], axis='rows'))
