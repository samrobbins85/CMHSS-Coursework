import requests
from bs4 import BeautifulSoup
import stanza
import re
import csv
from tqdm import tqdm
from OSGridConverter import grid2latlong
from nuts_finder import NutsFinder
import pandas as pd
import json
stanza.download('en') # download English model
nlp = stanza.Pipeline('en') # initialize English neural pipeline
# url = "https://historicengland.org.uk/listing/the-list/list-entry/1025190"

def details(tag):
    return type(tag.get("class")) is list and "nhle-list-entry__outer-container" in tag.get("class") and "Details" in [item.contents[0] for item in tag.find_all("h2")]

def extract_nouns(text):
    doc = nlp(text)
    nouns = []
    # For every sentence and word
    for sentence in doc.sentences:
        # Remove the last sentence with the listing details
        if sentence.text.startswith("Listing NGR"):
            continue
        for word in sentence.words:
            # If a non-proper noun or plural noun
            if word.xpos == "NN" or word.xpos == "NNS":
                # Add to list
                nouns.append(word)

    count = 0
    output = []

    while count<len(nouns):
        if nouns[count].deprel!="compound":
            if not re.match(r"c\d+", nouns[count].lemma):
                output.append(nouns[count].lemma)
        else:
            if not re.match(r"c\d+", nouns[count].lemma):
                if count+1<len(nouns):
                    if nouns[count].head== nouns[count+1].id:
                        output.append(nouns[count].lemma+ " "+ nouns[count+1].lemma)
                        count+=1
        count+=1
    return list(dict.fromkeys(output))


def proccess_url(soup, details):
    mydivs = soup.find(details)
    details=""
    for item in mydivs.children:
        if item.name=="h2" and item.contents[0] == "Details":
            details=item.findNext("p").get_text()
            break
    return extract_nouns(details)

def find_gr(tag):
    return tag.name=="dl" and "National Grid Reference:" in tag.find("dt")

def nuts(find_gr, soup, nf):
    mydivs = soup.find_all(find_gr)
    gr = mydivs[0].dd.contents[0].split(", ")[0]
    l=grid2latlong(gr)
    location = nf.find(lat=l.latitude, lon=l.longitude)
    if location == []:
        return False
    return location[1]["NUTS_ID"]


# big_list=[]

with open("improved_features_gt_5.json") as file:
    features = json.load(file)
nuts1_names = ["UKC", "UKD", "UKE", "UKF", "UKG", "UKH", "UKI", "UKJ", "UKK"]

out = {}

for item in features:
    out[item]={key: 0 for key in nuts1_names}
area_count = {key:0 for key in nuts1_names}


df = pd.DataFrame.from_dict(out)
nf = NutsFinder(year=2013, scale=60)

with open('NHLEExport.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in tqdm(reader):
        req = requests.get(dict(row)["Link"])
        soup = BeautifulSoup(req.content, 'html.parser')
        nouns = proccess_url(soup, details)
        nuts1 = nuts(find_gr, soup, nf)
        if nuts1:
            area_count[nuts1]+=1
            for item in nouns:
                if item in features:
                    df.loc[nuts1, item]+=1

df2=pd.DataFrame(area_count, index=[0])

df=df.div(df2.iloc[0], axis='rows')

jason = df.to_dict()

with open("improved_feature_stats.json", "w") as out_file:
    json.dump(jason,out_file, indent=2)

