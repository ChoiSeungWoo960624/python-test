import folium
import pandas as pd
import numpy as np
from geojson import Feature, FeatureCollection, Point, Polygon


#실무 실습
my_map=folium.Map(location=[36.678946, 127.896216], zoom_start=7,tiles="cartoDB positron")

#geoJSON   
geojson_data = "HangJeongDong_ver20241001.geojson"

folium.GeoJson(
    geojson_data,
    name="대한민국 경계",
    style_function=lambda _: {
        "fillColor": "blue",
        "color": "black",
        "weight": 1,
        "fillOpacity": 0.1,
    },
).add_to(my_map)
my_map.save("my_map.html")