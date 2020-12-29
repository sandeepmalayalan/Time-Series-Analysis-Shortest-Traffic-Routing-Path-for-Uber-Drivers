#presenting travel time in map for the selected time from LSTM output
label=[df1["source"][0],df1["destination"][0]]
n=round(dict2[int(HourlySelection)],2)
map1=folium.Map([lat1, lon1],zoom_start=17)
folium.Marker([lat1, lon1],popup=label[0]).add_to(map1)
folium.Marker([lat2, lon2],popup=label[1]).add_to(map1)
folium.PolyLine(locations=[(lat1,lon1),(lat2,lon2)],popup=str(n)+"minute").add_to(map1)
map1
