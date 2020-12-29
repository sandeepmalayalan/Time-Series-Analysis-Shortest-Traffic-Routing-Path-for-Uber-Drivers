from statsmodels.tsa.stattools import adfuller
stat = adfuller(inter_data["speed"].values)
print('ADF Statistic: %f' % stat[0])
print('p-value: %f' % stat[1])
  #p value is less than 0.05 so we rejected null hypothesis and its stationery
