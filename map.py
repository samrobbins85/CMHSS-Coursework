import pandas as pd
import json
from urllib.request import urlopen
import numpy as np
from tqdm import tqdm
# Code sourced from https://focaalvarez.medium.com/mapping-the-uk-and-navigating-the-post-code-maze-4898e758b82f
#Load GeoJson 
with open('new.geojson') as response:
    counties = json.load(response)
print("Geojson imported")
real_data=pd.read_json('improved_feature_stats.json')
entries = real_data.columns
real_data.index.name = 'nuts118cd'
real_data.reset_index(inplace=True)
#add dummy data
#With Plotly
import plotly.express as px
from geojson_rewind import rewind

#Make the rings clockwwise (to make it compatible with plotly)    
counties_corrected=rewind(counties,rfc7946=False)

for item in tqdm(entries):
    fig = px.choropleth(real_data, geojson=counties_corrected, locations='nuts118cd', featureidkey="properties.nuts118cd", color=item,
                                color_continuous_scale="PurPor", labels={'label name':'label name'}, title=item.capitalize(),
                                scope="europe")
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.write_image("improved_big_images/"+item+".png")
# fig.show()