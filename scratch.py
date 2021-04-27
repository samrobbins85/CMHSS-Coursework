import pandas as pd

data1 = {"UKC":[1.,3.,5.,2.],
         "UKD":[4.,8.,3.,7.],
         "UKE":[5.,45.,67.,34]}
data2 = {"a":[4.],
         "b":[2.],
         "c":[11.]}

nuts1 = ["UKC", "UKD", "UKE"]
area_count = {key:2 for key in nuts1}
df2=pd.DataFrame(area_count, index=[0])

df1 = pd.DataFrame(data1).T
print(df1)
print(df2.iloc[0])

print(df1.div(df2.iloc[0], axis='rows'))