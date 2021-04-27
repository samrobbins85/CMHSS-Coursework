from OSGridConverter import grid2latlong
from nuts_finder import NutsFinder
from bs4 import BeautifulSoup
import requests

def details(tag):
    return tag.name=="dl" and "National Grid Reference:" in tag.find("dt")

url="https://historicengland.org.uk/listing/the-list/list-entry/1117776"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
mydivs = soup.find_all(details)
gr = mydivs[0].dd.contents[0].split(", ")[0]
nf = NutsFinder()
l=grid2latlong(gr)
print(nf.find(lat=l.latitude, lon=l.longitude))