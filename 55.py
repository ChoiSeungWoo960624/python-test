import folium
from geojson import Feature, FeatureCollection, Point, Polygon
'''
#지도 열기
my_map = folium.Map(locatuo=[37.552241, 126.995946], zoom_start=12) #마커 등록할때 좋음
my_map.save("my_map.html")

#지도 스타일 추가
my_map = folium.Map(locatuo=[37.552241, 126.995946], zoom_start=12, tiles="CartoDB positron") # 영역이 필요할 때 회색 지도 유리
my_map.save("my_map.html")


my_map = folium.Map(locatuo=[37.552241, 126.995946], zoom_start=12, tiles="CartoDB positron")

folium.Marker([37.607284, 127.056631], popup="집앞").add_to(my_map) #기본마커
folium.Marker([37.599198, 127.051068], popup="평화의전당", icon=folium.Icon(color="red", icon="home")).add_to(my_map) #홈설정
my_map.save("my_map.html")


# 지도에 여러개 마커 딕셔너리 형태로 추가
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

#지도에 영역 표시
my_map = folium.Map(locatuo=[37.552241, 126.995946], zoom_start=12, tiles="CartoDB positron")

#원형영역
folium.Circle(location= [37.596180, 127.063689], radius=300, color="blue", popup="외대앞역 일대", fill=True, fill_color="yellow").add_to(my_map)
#radius - 거리영역(반지름)

my_map.save("my_map.html")    



#GeoJSON

#데이터 생성
feature1 = Feature(geometry=Point((127.093242 ,37.553828)), properties={"name": "서울", "populatuon": "970만"})
feature2 = Feature(geometry=Point((126.637199 ,33.266597)), properties={"name": "제주도", "populatuon": "10만"})
feature3 = Feature(geometry=Point((127.526064 ,37.415474)), properties={"name": "경기도", "populatuon": "2000만"})
feature4 = Feature(geometry=Point((128.323530 ,37.923473)), properties={"name": "강원도", "populatuon": "500만"})
 
#데이터 하나로 묶기
geojson_data = FeatureCollection([feature1, feature2, feature3, feature4])

# 지도생성
my_map = folium.Map(location=[36.616051, 127.970818], zoom_start=9)

# 데이터를 지도에 추가
folium.GeoJson(geojson_data, name="GeoJSON Data", tooltip=folium.GeoJsonTooltip(fields=["name", "population"], aliases=["도시이름: ", "인구: "]),).add_to(my_map)

my_map.save("my_map.html")
'''

