#Arima model
!pip install pyramid-arima
import pandas as pd
from statsmodels.tsa.stattools import acf
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
from math import sqrt
import warnings
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
warnings.simplefilter("ignore")
y=inter_data.values
train=y[0:720]
aic=list()
pdq=list()
for p in range(7):
  for d in range(2):
    for q in range(4):
      try:
        order = (p,d,q)
        arima_mod=ARIMA(train,order)
        mode=arima_mod.fit()
        aic.append(mode.aic)
        pdq.append(order)
      except:
        continue
if(len(aic)>0):
  mini=min(aic)
  pd1=aic.index(mini)
  mini1=pdq[pd1]
  print(mini,mini1) 
  #Arima model prediction
warnings.simplefilter("ignore")
y=inter_data.values
train=y[0:720]
test1=y[696:720]
test=y[720:]
pred=[]
training_data = [x for x in train]
for i in range(0,len(test1)):
  model = ARIMA(training_data,order=mini1)
  model_fit = model.fit(disp=0)
  yhat = model_fit.forecast()
  pred.append(yhat[0])
  training_data.append(test1[i])
error = sqrt(mean_squared_error(test, pred))
arima=round(error,2)
print("rmse is",arima)
