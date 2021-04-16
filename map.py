import pandas as pd
import json
from urllib.request import urlopen
import numpy as np
# Code sourced from https://focaalvarez.medium.com/mapping-the-uk-and-navigating-the-post-code-maze-4898e758b82f
#Load GeoJson 
with open('nuts1.geojson') as response:
    counties = json.load(response)
 
#Load data to be charted    
dummy_data=pd.read_csv('nuts1.csv')
#add dummy data
dummy_data['value']=np.random.randint(10, 100, size=len(dummy_data))

#With Plotly
import plotly.express as px
from geojson_rewind import rewind

#Make the rings clockwwise (to make it compatible with plotly)    
counties_corrected=rewind(counties,rfc7946=False)

fig = px.choropleth(dummy_data, geojson=counties_corrected, locations='nuts118cd', featureidkey="properties.nuts118cd", color='value',
                            color_continuous_scale="PurPor", labels={'label name':'label name'}, title='MAP TITLE',
                            scope="europe")

fig.update_geos(fitbounds="locations", visible=False)
fig.write_image("fig1.png")