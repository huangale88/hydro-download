import folium
from geopy.geocoders import Nominatim
from pyproj import CRS, Transformer
from IPython.display import display, HTML
from folium.plugins import Geocoder
from folium.plugins import MiniMap
from folium.plugins import MeasureControl
from folium.plugins import Draw
from folium import Figure
import requests
import geopandas as gpd
import webbrowser


'''
# Define a function to handle the map click event
def on_click(event):
    lat, lon = event['latlng']
    print(f"Latitude: {lat}, Longitude: {lon}")

    # Define NAD83 (EPSG:4269) and get projection (EPSG code)
    crs = CRS.from_epsg(4269)
    transformer = Transformer.from_crs(crs, crs)
    projection = crs.to_epsg()

    print(f"Projection: {projection}")
'''

# Create the map and add features
fig = Figure(width=1000, height=600)
m = folium.Map(location=[49.1386, -123.0139], zoom_start=10)
folium.TileLayer("Esri.WorldImagery").add_to(m)
folium.TileLayer("OpenTopoMap").add_to(m)
folium.TileLayer("OpenStreetMap").add_to(m)
# m.add_child(folium.LatLngPopup())
m.add_child(folium.ClickForLatLng(format_str='"[" + lat + "," + lng + "]"', alert=True))
Geocoder().add_to(m)

# Add WMS layer to the same map instance
folium.WmsTileLayer(
    url="https://geo.weather.gc.ca/geomet-climate/?service=WMS&version=1.3.0&request=GetCapabilities",
    name="climate",
    fmt="image/png",
    layers="CLIMATE.STATIONS",
    attr=u"stations",
    transparent=True,
    overlay=True,
    control=True,
).add_to(m)

# Add a collapsible minimap
MiniMap(toggle_display=True).add_to(m)

# Add a measuring tool
m.add_child(MeasureControl())

'''
# Add a draw function
Draw(export=True).add_to(m)
file_path = 'your_file.geojson'
m.save(file_path)
'''

# Add LayerControl after all layers have been added
folium.LayerControl().add_to(m)

fig.add_child(m)
m.save('map.html')
webbrowser.open('map.html')