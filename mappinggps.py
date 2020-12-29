#Mapping latitude and longitude to the records
final=pd.DataFrame(columns=['slat', 'slon','elat', 'elon', 'start_osm','end_osm','speed','date'])
lis=[]
for i,j,k,l,m,n in zip(data3["start_junction_id"],data3["end_junction_id"],data3["start_osm"],data3["end_osm"],data3["speed"],data3["date"]):
  l2=[]
  l3=[]
  b=False
  b1=False
  slat=None
  slon=None
  elat=None
  elon=None
  for i1,j1,k1 in zip(junc["lat"],junc["lon"],junc["osm_id"]):
    if k1==k:
      slat=i1
      slon=j1
      l2=[slat,slon]
    if k1==l:
      elat=i1
      elon=j1
      l3=[elat,elon]
  if slat!=None and slon!=None and elat!=None and elon!=None:
    final=final.append({'start_osm':k,'end_osm':l,'slat':slat,'slon':slon,'elat':elat,'elon':elon,'speed':m,'date':n}, ignore_index=True)
    for p in lis:
      if p[0]==l2[0] and p[1]==l2[1]:
        b=True
    if b==False:
      lis.append(l2)
    for p in lis:
      if p[0]==l3[0] and p[1]==l3[1]:
        b1=True
    if b1==False:
      lis.append(l3)    
