import requests
from bs4 import BeautifulSoup
import stanza
import re
import csv
from tqdm import tqdm
import collections
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
                if len(nouns)<count:
                    if nouns[count].head== nouns[count+1].id:
                        output.append(nouns[count].lemma+ " "+ nouns[count+1].lemma)
                        count+=1
        count+=1
    return list(dict.fromkeys(output))


def proccess_url(url, details):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    mydivs = soup.find(details)
    details=""
    for item in mydivs.children:
        if item.name=="h2" and item.contents[0] == "Details":
            details=item.findNext("p").get_text()
            break
    return extract_nouns(details)

big_list=[]

with open('NHLEExport.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in tqdm(reader):
        nouns = proccess_url(dict(row)["Link"], details)
        big_list+=nouns

print(collections.Counter(big_list))

