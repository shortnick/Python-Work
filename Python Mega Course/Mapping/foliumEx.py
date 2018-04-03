#! python3

import folium as fol


carto = fol.Map(location=[47.6062100, -122.3320700], zoom_start=10)
fg= fol.FeatureGroup(name="Living Quarters")

places = [[47.614851, -122.346965], [47.590428, -122.312433], [47.670215, -122.321063]]
for coordinates in places:
	fg.add_child(fol.Marker(location=coordinates, popup="Living in Seattle", icon=fol.Icon(color='green')))


carto.add_child(fg)
carto.save("homeMap.html")
