#! python3

import folium as fol
import pandas as pd
import os

scriptpath = os.getcwd()
volcfile = os.path.join(scriptpath, "Example files\\Volcanoes_USA.txt")
worldfile = os.path.join(scriptpath, "Example files\\world.json")


volcs = pd.read_csv(str(volcfile))
lat = list(volcs["LAT"])
longi = list(volcs["LON"])
named = list(volcs["NAME"])
elev= list(volcs["ELEV"])
stat= list(volcs["STATUS"])
html = """<p>Volcano: </p> %s <p> is </p> %s <p>meters.</p>"""

def colorPicker(altitude):
	if altitude <1000:
		return 'green'
	elif 1000<=altitude<2000:
		return 'orange'
	elif altitude >=2000:
		return 'red'
	else:
		return 'pink'


carto = fol.Map(location=[42, -117.026], zoom_start=5)
vfg= fol.FeatureGroup(name="Volcanoes")

places = [[47.614851, -122.346965], [47.590428, -122.312433], [47.670215, -122.321063]]
for lat, lon, n, el in zip(lat, longi, named, elev):

	iframe = fol.IFrame(html=html % (str(n), str(el)), width=300,height=100)
	try:
		vfg.add_child(fol.CircleMarker(location=[lat,lon], popup=fol.Popup(iframe), color='lightgray', fill_color=colorPicker(el), fill=True, fill_opacity=0.5, radius=5))
	except:
		print("Problem "+n) 

pfg= fol.FeatureGroup(name="Population")

pfg.add_child(fol.GeoJson(data=(open(worldfile, 'r', encoding='utf-8-sig').read()), style_function=lambda x:{'fillColor':'cyan' if x['properties']['POP2005']<10000000 else 'purple' if x['properties']['POP2005']<100000000 else 'green'}))

carto.add_child(vfg)
carto.add_child(pfg)
carto.add_child(fol.LayerControl())
carto.save("VolcanoMap.html")