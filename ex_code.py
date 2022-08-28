import pandas as pd
import datatable as dt
import numpy as np
import geopandas as gpd
import seaborn as sns
import pydeck as pdk
import json 
from tqdm import tqdm 
import gc
import os
mapbox_api_token = os.getenv("MAPBOX_ACCESS_TOKEN")


dat = pd.read_csv('F:/SeoulHotPlace/final.csv', encoding='cp949')

def click(df, top, month, day, time, sex):
    new_df = df[(df['대상연월'] == month) &
                     (df['요일'] == day) &
                     (df['time'] == time) &
                     (df['성별'] == sex)]
    new_df = new_df.sort_values('이동인구(합)', ascending=False)
    new_df['normalized_이동인구'] = new_df['이동인구(합)'] / new_df['이동인구(합)'].max()
    new = new_df.iloc[0:top,:].copy()
    new.reset_index(drop=True, inplace=True)
    
    layer = pdk.Layer(
        'ArcLayer',
        new,
        get_source_position='start_point',
        get_target_position='end_point',
        get_width='1 + 100 * normalized_이동인구',
        get_source_color='[255, 255, 120]',
        get_target_color='[255, 0, 255]',
        pickable=True,
        auto_highlight=True
    )
    
    center = [126.986, 37.565]
    view_state = pdk.ViewState(longitude=center[0], latitude=center[1]) 
    view_state.zoom = 10
    view_state.bearing = -15
    view_state.pitch = 45
    
    r = pdk.Deck(layers=[layer], initial_view_state=view_state, mapbox_key = mapbox_api_token)
    r.to_html("F:/SeoulHotPlace/c.html", open_browser=True)

    return new
new = click(dat, 500, 202204, '토', '점심', 'F')