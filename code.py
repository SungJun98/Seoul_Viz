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
MAPBOX_API_KEY = 'pk.eyJ1IjoiYm94Ym94NCIsImEiOiJjbDZtdnE5bXIwNnYyM2dwY2g5dHNqdmVpIn0.uecpQOA7rJmPrsBzo0WM-A'

# 대한민국 행정동 경계 파일 
# https://github.com/vuski/admdongkor/tree/master/ver20220401
geo_data = 'F:/SeoulHotPlace/dataset/HangJeongDong_ver20220401.txt'
with open(geo_data,encoding="UTF-8") as json_file:   
    df = gpd.read_file(json_file)

df = df.iloc[:,[0,1,2,10]]

def multipolygon_to_coordinates(x):
    lon, lat = x[0].exterior.xy
    return [[x, y] for x, y in zip(lon, lat)]
df['coordinates'] = df['geometry'].apply(multipolygon_to_coordinates)
del df['geometry']

# 각 행정동 별 가운데 좌표 생성 
lst = []
for i in df['coordinates']:
    idx_1 = 0
    idx_2 = 0
    for j in i:
        idx_1 += j[0]
        idx_2 += j[1]
    lst.append([idx_1 / len(i), idx_2 / len(i)])

df['MiddlePoint'] = lst
middle = df[['adm_cd', 'adm_nm', 'MiddlePoint']]
middle['adm_cd'] = pd.to_numeric(middle['adm_cd'])
del df

# 데이터 규합 
def preprocess(df):
    data = df.copy()
    data = data[(data['출발 행정동 코드'] >= 1100000) & 
                (data['출발 행정동 코드'] <= 1200000) & 
                (data['도착 행정동 코드'] >= 1100000) & 
                (data['도착 행정동 코드'] <= 1200000)] # 서울시 내부 이동 필터링 

    data.loc[data['이동인구(합)'] == '*', '이동인구(합)'] = 3  # * 표시는 3명 이하라는 뜻이므로 3으로 대체 
    data = data[data['이동유형'].isin(['EE', 'HE', 'WE'])] # 집과 직장이 목적인 경우 제외하고 나머지 이동 경로만
    data = data[data['나이'].isin([15,20,25,30,35])] 
    data.drop(['평균 이동 시간(분)', '이동유형', '나이'], axis=1, inplace=True)
    data.reset_index(drop=True, inplace=True)
    
    return data

def month_fit(path):
    df_list = os.listdir(path)
    final = pd.DataFrame()
    for i in tqdm(df_list):
        data = pd.read_csv(path + '\{}'.format(i), encoding='cp949')
        data = preprocess(data)
        final = pd.concat([final, data])
        del data 
    conditionlist = [    
        (final['도착시간'].isin([3,4,5,6])), (final['도착시간'].isin([7,8,9,10])),
        (final['도착시간'].isin([11,12,13,14])), (final['도착시간'].isin([15,16,17,18])),
        (final['도착시간'].isin([19,20,21,22])), (final['도착시간'].isin([23,0,1,2]))]
    choicelist = ['새벽', '아침', '점심', '오후', '저녁', '밤']
    final['time'] = np.select(conditionlist, choicelist, default='Not Specified')
    final['이동인구(합)'] = pd.to_numeric(final['이동인구(합)'])
    final = final.groupby(['대상연월', '요일', 'time','출발 행정동 코드', 
                           '도착 행정동 코드', '성별'])['이동인구(합)'].sum().reset_index()
    final = pd.merge(final, middle, left_on='출발 행정동 코드', right_on='adm_cd',how='left').dropna(axis=0)
    final = pd.merge(final, middle, left_on='도착 행정동 코드', right_on='adm_cd',how='left').dropna(axis=0)
    final = final.rename(columns = {'MiddlePoint_x' : 'start_point', 'MiddlePoint_y' : 'end_point'})
    final.drop(['adm_cd_x', 'adm_cd_y'], axis=1, inplace=True)
    
    return final

path = 'F:\SeoulHotPlace\dataset\data'
path_list = os.listdir(path)
final = pd.DataFrame()
for idx in tqdm(path_list):
    path_2 = path+'\{}'.format(idx)
    dat = month_fit(path_2)
    final = pd.concat([final, dat])
    del dat
final.reset_index(drop=True, inplace=True)

final.to_csv(r'F:\SeoulHotPlace\final.csv', encoding='cp949', index=False)





dat = pd.read_csv(r'F:\SeoulHotPlace\final.csv', encoding='cp949')

def click(df, top, month, day, time, sex):
    new_df = df[(df['대상연월'] == month) &
                     (df['요일'] == day) &
                     (df['time'] == time) &
                     (df['성별'] == sex)].copy()
    new_df = new_df.sort_values('이동인구(합)', ascending=False)
    new_df['normalized_이동인구'] = new_df['이동인구(합)'] / new_df['이동인구(합)'].max()
    new = new_df.iloc[0:top,:].copy()
    
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
    view_state.zoom = 12
    view_state.bearing = -15
    view_state.pitch = 45
    
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    r.to_html("F:/SeoulHotPlace/b.html",open_browser=True)

    return new
click(final, 500, 202204, '토', '점심', 'F')



click(dat, 500, 202204, '토', '점심', 'F')







new.to_csv(r'F:\SeoulHotPlace\new.csv', encoding='cp949', index=False)

# plotly dash 웹 배포 : https://dschloe.github.io/python/dash/dash_project/




