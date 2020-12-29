import osmapi as osm
import geocoder
junc=pd.DataFrame(columns=['lat','lon','osm_id'])
api = osm.OsmApi()
jun=set(list(data3["start_osm"])+list(data3["end_osm"]))
n1=list(jun)
print(n1)
for i in n1:
  print(i)
  node1 = api.NodeGet(i)
  junc=junc.append({'lat':node1["lat"],'lon':node1["lon"],'osm_id':i},ignore_index=True)
print(junc)
