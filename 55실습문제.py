import folium
import pandas as pd
import numpy as np
from geojson import Feature, FeatureCollection, Point, Polygon

'''
#1
my_map = folium.Map(locatuo=[37.552241, 126.995946], zoom_start=12, tiles="CartoDB positron")
map_info = [
    {"location": [37.596180, 127.063689], "popup": "외대앞역"},
    {"location": [37.602037, 127.067638], "popup": "신이문역"},
    {"location": [37.589732, 127.057578], "popup": "회기역"},
    {"location": [37.610557, 127.055987], "popup": "돌곶이역"},
    {"location": [37.602599, 127.079177], "popup": "중화역"},
    ]

for info in map_info:
    folium.Marker(location=info["location"], popup=info["popup"], icon=folium.Icon(color="blue", icon="arrow-down")).add_to(my_map)

my_map.save("my_map.html")


df = pd.DataFrame([[37.596180, 127.063689],[37.602037, 127.067638], [37.589732, 127.057578], [37.610557, 127.055987], [37.602599, 127.079177]],
                 index=["외대앞역","신이문역", "회기역", "돌곶이역", "중화역"],
                 columns=["지하철", "위도"]
                 )

print(df)

#subway.csv 파일로 저장하는 방법
df.to_csv("subway.csv", encoding="EUC-KR", index=False) # index=False 이걸 해야 앞에 숫자가 안 붙음

#1번 문제 솔루션.
# 실습
# 서울 지하철 5개

data = {
    "Station": ["서울역", "공덕역", "응암역", "홍대입구역", "디지털미디어시티역"],
    "Latitude": [37.555044, 37.542723, 37.598571, 37.557412, 37.576269],
    "Longitude": [126.970741, 126.951833, 126.915525, 126.924493, 126.901534],
}
subway = pd.DataFrame(data)
# csv파일저장
subway.to_csv("subway.csv", encoding="EUC-KR", index=False)
# folium 지도제작
my_map = folium.Map(location=[37.580307, 126.928719], zoom_start=12)
# 방법1
# subway.apply(
#     lambda x: folium.Marker(
#         location=[x["Latitude"], x["Longitude"]],
#         popup=x["Station"],
#         icon=folium.Icon(color="blue", icon="home"),
#     ).add_to(my_map),
#     axis=1, # 열단위로 작업. axis=0 행단위로 작업
# )
# 방법2
# iterrow() : 데이터프레임에서 행단위로 반복하면서 인덱스와 행의 쌍을 반환하는 함수
for _, x in subway.iterrows():
    folium.Marker(
        location=[x["Latitude"], x["Longitude"]],
        popup=x["Station"],
        icon=folium.Icon(color="blue", icon="star"),
    ).add_to(my_map)

my_map.save("my_map.html")
'''
'''
FeatureCollection :
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            127.10204379440478,
            37.16244471540077
          ],
          [
            126.43683698841642,
            37.44764095049305
          ],
          [
            126.7415190234808,
            37.84485399934671
          ]
        ],
        "type": "LineString"
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            126.74566904784234,
            37.843135067046035
          ],
          [
            127.04872226838665,
            37.903544031966746
          ],
          [
            127.32598673740898,
            37.613997990408095
          ],
          [
            127.10117059480524,
            37.1687958082269
          ]
        ],
        "type": "LineString"
      }
    }
  ]
}
'''


maps_data = Feature(geometry=Polygon([[[127.10204379440478, 37.16244471540077], [126.43683698841642, 37.44764095049305], [126.7415190234808, 37.84485399934671], [126.74566904784234, 37.843135067046035], [127.04872226838665, 37.903544031966746], [127.32598673740898, 37.613997990408095], [127.10117059480524,37.1687958082269],]]), properties={"name": "서울"})

my_map = folium.Map(location=[36.616051, 127.970818], zoom_start=9)
folium.GeoJson(maps_data, name="수도권", tooltip=folium.GeoJsonTooltip(fields=["name"], aliases=["영역의 이름: "]), style_function=lambda x : {
    "fillcolr": "yellow", #다각형 내부 색상
    "color": "black", # 테두리 색상
}).add_to(my_map)

my_map.save("my_map.html")