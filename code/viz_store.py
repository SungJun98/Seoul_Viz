# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 15:47:14 2022

@author: SungJunLim
"""
import pandas as pd
import pydeck as pdk
import os

os.chdir(r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz')
MAPBOX_API_KEY = 'pk.eyJ1IjoibHNqOTg2MiIsImEiOiJja3dkNjMxMDczOHd1MnZtcHl0YmllYWZjIn0.4IFNend5knY9T_h3mv8Bwg'

'''
### 1. Naver Top100
# 1.1. Load Data
df_1 = pd.read_csv(r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\data\naver_Gabozza_detail.csv')
coordinates = [[x, y] for x, y in zip(df_1.longitude, df_1.latitude)]
df_1['coordinates'] = coordinates
df_1 = df_1.drop(['Unnamed: 0'], axis=1)

NAVER_ICON_URL = 'https://s.pstatic.net/static/www/mobile/edit/2016/0705/mobile_212852414260.png'
icon_data = {
    "url": NAVER_ICON_URL,
    "width": 128,
    "height": 128,
    "anchorY": 128,
}

df_1['icon'] = None
for i in df_1.index:
    df_1["icon"][i] = icon_data

# 1.2. Make Layer
icon_layer_1 = pdk.Layer(
    type="IconLayer",
    data=df_1,
    get_icon="icon",
    get_size=4,
    size_scale=3,
    get_position='coordinates',
    pickable=True,
    auto_highlight=True
)
'''


'''
icon 그려지지 않는 오류 참고 reference
# https://github.com/visgl/deck.gl/issues/3900
# https://stackoverflow.com/questions/6375942/how-do-you-base-64-encode-a-png-image-for-use-in-a-data-uri-in-a-css-file
'''
import base64

def image_to_data_url(filename):
    ext = filename.split('.')[-1]
    prefix = f'data:image/{ext};base64,'
    with open(filename, 'rb') as f:
        img = f.read()
    return prefix + base64.b64encode(img).decode('utf-8')

'''
### 2. OliveYoung
# 2.1. Load Data
df_2 = pd.read_csv(r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\data\oliveyoung.csv')
coordinates = [[x, y] for x, y in zip(df_2.longitude, df_2.latitude)]
df_2['coordinates'] = coordinates

OLIVEYOUNG_ICON = r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\data\oliveyoung_logo.png'

icon_64 = image_to_data_url(OLIVEYOUNG_ICON)

icon_data = {
    "url": icon_64,
    "width": 128,
    "height": 128,
    "anchorY": 128,
}

df_2['icon_data'] = None
for i in df_2.index:
    df_2["icon_data"][i] = icon_data

# 2.2. Make Layer
icon_layer_2 = pdk.Layer(
    type="IconLayer",
    data=df_2,
    get_icon="icon_data",
    get_size=4,
    size_scale=3,
    get_position='coordinates',
    pickable=True,
    auto_highlight=True
)
'''



### 3. Subway
# 3.1. Load Data
df_3 = pd.read_csv(r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\data\subway.csv')
coordinates = [[x, y] for x, y in zip(df_3.longitude, df_3.latitude)]
df_3['coordinates'] = coordinates
df_3 = df_3.drop(['Unnamed: 0'], axis=1)

SUBWAY_ICON_URL = r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\data\subway_logo.png'

icon_64 = image_to_data_url(SUBWAY_ICON_URL)

icon_data = {
    "url": icon_64,
    "width": 128,
    "height": 128,
    "anchorY": 128,
}

df_3['icon_data'] = None
for i in df_3.index:
    df_3["icon_data"][i] = icon_data

# 3.2. Make Layer
icon_layer_3 = pdk.Layer(
    type="IconLayer",
    data=df_3,
    get_icon="icon_data",
    get_size=4,
    size_scale=3,
    get_position='coordinates',
    pickable=True,
    auto_highlight=True
)


'''
### 4. BurgerKing
# 4.1. Load Data
df_4 = pd.read_csv(r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\data\burgerking.csv')
coordinates = [[x, y] for x, y in zip(df_4.longitude, df_4.latitude)]
df_4['coordinates'] = coordinates
df_4 = df_4.drop(['Unnamed: 0'], axis=1)

BURGERKING_ICON = r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\data\burgerking_logo.png'
icon_64 = image_to_data_url(BURGERKING_ICON)

icon_data = {
    "url": icon_64,
    "width": 128,
    "height": 128,
    "anchorY": 128,
}

df_4['icon_data'] = None
for i in df_4.index:
    df_4["icon_data"][i] = icon_data

# 4.2. Make Layer
icon_layer_4 = pdk.Layer(
    type="IconLayer",
    data=df_4,
    get_icon="icon_data",
    get_size=4,
    size_scale=3,
    get_position='coordinates',
    pickable=True,
    auto_highlight=True
)
'''


### Set the viewport location
center = [126.986, 37.565]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

# Render
r = pdk.Deck(layers=[icon_layer_1, icon_layer_2, icon_layer_3, icon_layer_4], initial_view_state=view_state)
r.to_html('demo.html')

# oliveyoung, subway, burgerking은 다 안 된다....