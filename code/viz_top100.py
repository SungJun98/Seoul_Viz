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

# Load Data
df = pd.read_csv(r'C:\Users\SungJunLim\Desktop\Lim\UOS\Side-Project\Seoul_Viz\crawled_data\naver_Gabozza_detail.csv')
coordinates = [[x, y] for x, y in zip(df.longitude, df.latitude)]
df['coordinates'] = coordinates
df = df.drop(['Unnamed: 0'], axis=1)
df.head()


# Make layer
layer = pdk.Layer(
    'ScatterplotLayer', # 사용할 Layer 타입
    df, # 시각화에 쓰일 데이터프레임
    get_position='coordinates', # geometry 정보를 담고있는 컬럼 이름
    get_radius=50,
    get_fill_color='[255,255,255]',
    pickable=True, # 지도와 interactive 한 동작 on
    auto_highlight=True # 마우스 오버(hover) 시 박스 출력
)

# Set the viewport location
center = [126.986, 37.565]
view_state = pdk.ViewState(
    longitude=center[0],
    latitude=center[1],
    zoom=10)

# Render
r = pdk.Deck(layers=[layer], initial_view_state=view_state)
r.to_html('demo.html')

# 서울 경계를 그려주면 아주 나이스하겠는걸요?!