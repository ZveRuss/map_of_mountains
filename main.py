# Import Library
import folium
import pandas as pd

# Create base map
map_test = folium.Map(location=[37.296933, -121.9574983], zoom_start=5)

# Read data of Volcanoes USA
data = pd.read_csv('./data/Volcanoes_USA.txt')
lat = data['LAT']
lon = data['LON']
elevation = data['ELEV']


def color_change(elev):
    if elev < 1000:
        return 'green'
    elif 1000 <= elev <= 3000:
        return 'orange'
    else:
        return 'red'

# Add Markers
for LAT, LON, ELEV in zip(lat, lon, elevation):
    folium.CircleMarker(location=[LAT, LON], radius=9, popup=str(ELEV) + 'm', fill_color=color_change(ELEV),
                        color="gray", fill_opacity=0.9).add_to(map_test)

# Save the map
map_test.save("map1.html")
