from bs4 import BeautifulSoup
import requests
def details(tag):
    return type(tag.get("class")) is list and "nhle-list-entry__outer-container" in tag.get("class") and "Details" in [item.contents[0] for item in tag.find_all("h2")]

# def details1(tag):
#     if(type(tag.get("class")) is list and "nhle-list-entry__outer-container" in tag.get("class")):
#         h2s = tag.find_all("h2")
#         print([item.contents[0] for item in tag.find_all("h2")])
#         # for item in h2s:
#         #     print(item.contents)
#     return type(tag.get("class")) is list and "nhle-list-entry__outer-container" in tag.get("class")

url="https://HistoricEngland.org.uk/listing/the-list/list-entry/1025190"

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
mydivs = soup.find(details)
details=""
for item in mydivs.children:
    if item.name=="h2" and item.contents[0] == "Details":
        details=item.findNext("p").get_text()
        break
print(details)
