import folium
import pandas as pd
import numpy as np
from geojson import Feature, FeatureCollection, Point, Polygon


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