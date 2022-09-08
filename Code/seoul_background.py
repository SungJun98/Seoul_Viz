import numpy as np
import pandas as pd
import geopandas as gpd
import pydeck as pdk

df = gpd.read_file('https://raw.githubusercontent.com/heumsi/geo_data_visualisation_introduction/master/data/older_seoul.geojson')

def multipolygon_to_coordinates(x):
    lon, lat = x[0].exterior.xy
    return [[x, y] for x, y in zip(lon, lat)]

df['coordinates'] = df['geometry'].apply(multipolygon_to_coordinates)

del df['geometry']
del df['인구']
del df['남자']
del df['여자']

df = pd.DataFrame(df)

layer = pdk.Layer(
    'PolygonLayer',
    df,
    get_polygon = 'coordinates',
    get_fill_color = '[128, 128, 128]',
    pickable = True,
    auto_highlight = True,
    opacity = 0.05
)

center = [126.986, 37.565]

view_state = pdk.ViewState(
    longitude = center[0],
    latitude = center[1],
    zoom = 10)

# Render
r = pdk.Deck(layers = [layer1], initial_view_state = view_state)
r.to_html()