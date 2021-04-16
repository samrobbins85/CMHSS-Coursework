from OSGridConverter import grid2latlong
from nuts_finder import NutsFinder
nf = NutsFinder()
l=grid2latlong('NZ 23272 59118')
print(nf.find(lat=l.latitude, lon=l.longitude))