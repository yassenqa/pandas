import pandas as p 
import numpy as np 
date=p.to_datetime("15th of march, 2022 ")
print(date)
print('.'*25)
date=p.to_datetime("15th of march, 2022 ")
y=date+p.to_timedelta(np.arange(20),'D')
print(date)
print(y)

print('.'*25)
index=p.to_datetime(['2014-07-04 ','2014-08-04','2014-07-04','2015-08-04'])
d=p.Series([0,1,2,3],index=index)
print(d)

print('.'*25)
index=p.to_datetime(['2014-07-04 ','2014-08-04','2014-07-04','2015-08-04'])
d=p.Series([0,1,2,3],index=index)
print(d['2014-01-01':'2014-12-31'])

print('.'*25)
date=p.date_range('2011-03-15','2011-04-21')
print(date)

print('.'*25)
date=p.date_range('2011-03-15',periods=8)#8 day after the date
print(date)

print('.'*25)
date=p.date_range('2011-03-15',periods=8,freq='h')#8 houers after the date also take M Y
print(date)


print('.'*25)
date=p.timedelta_range(0,periods=50, freq='d')#(start , , )counting day
print(date)


print('.'*25)
date=p.timedelta_range(0,periods=25, freq='h')#(start , , )counting day
print(date)

print('.'*25)
date=p.timedelta_range(0,periods=25, freq='2h30t40s')#(start , , )counting day
print(date)
print('.'*25)

from pandas.tseries.offsets import BDay
data=p.date_range('2222-02-22',periods=5,freq=BDay())#international
print(data)



