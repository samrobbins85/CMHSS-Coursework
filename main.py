import requests
from bs4 import BeautifulSoup

url = "https://historicengland.org.uk/listing/the-list/list-entry/1025190"

def details(tag):
    return type(tag.get("class")) is list and "nhle-list-entry__outer-container" in tag.get("class") and "Details" in tag.contents[1].contents

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
# mydivs = soup.find_all("div", {"class": "nhle-list-entry__outer-container"})
mydivs = soup.find_all(details)
print(mydivs[0].p.get_text())
# print(soup.prettify())