#Interpolating data to make it stationary and filtered into one source and destination records

df11=df1[df1["source"]==df1["source"][0]]
df11=df11.sort_values(by=['date'])
df2=df11[["date","speed"]]
df2["date"] = df2["date"].apply(lambda x:datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'))
df2["date"]=df2["date"].apply(lambda x:x.replace(minute=0, second=0))
k=df2[["date","speed"]]
print(k)

kk=pd.date_range('10/1/2018', periods = 744, freq ='H')
df9=pd.DataFrame(columns=['speed','date'])
df9['speed'].fillna(method='ffill')
df9['date']=kk[0:744]
pd.to_numeric(df9['speed'])
for i,j in zip(df2['speed'],df2['date']):
  for k,l in zip(df9['date'][0:744],df9.index):
    if j.day==k.day and j.hour==k.hour:
      df9.ix[l, 'speed'] = i

df9.set_index("date",inplace=True)
df9['speed']=pd.to_numeric(df9["speed"])
inter_data = df9.interpolate(method='linear',limit_direction='both')
