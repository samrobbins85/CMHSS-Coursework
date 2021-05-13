
from nuts_finder import NutsFinder
nf = NutsFinder(year=2013)  # <-- expect a little bit of loading time here whilst it downloads some shapefiles
print(nf.find(lat=53.406115, lon=-2.965604))  # <-- pretty quick 