import pandas as p 
import numpy as np
d=p.DataFrame({'emp':['bob','bilal','yassen','lisa'],'group':['sql','data','php','desgin']})

d1=p.DataFrame({'emp':['bilal','bob','yassen','lisa'],'date':[1999,1988,2001,2004]})
print(d)
print(d1)

d2=p.merge(d,d1)
print(d2)

print('!'*50)
d=p.DataFrame({'emp':['bob','bilal','yassen','lisa'],'group':['sql','data','php','desgin']})

d1=p.DataFrame({'emp':['bilal','hosam','bassil','mohammad'],'date':[1999,1988,2001,2004]})
print(d)
print(d1)

d2=p.merge(d,d1)
d3=p.merge(d,d1,how='inner')
d4=p.merge(d,d1,how='outer')
d5=p.merge(d,d1,how='right')
d6=p.merge(d,d1,how='left')

print(d2)

print('.'*25)
print(d3)
print('.'*25)

print(d4)
print('.'*25)
print(d5)
print('.'*25)
print(d6)

print('!'*50)
d=p.DataFrame({'emp':['bob','bilal','yassen','lisa'],'group':['sql','data','php','desgin']})

d1=p.DataFrame({'name':['yassen','bilal','bob','lisa'],'date':[1999,1988,2001,2004]})
print(d)
print(d1)

print(p.merge(d,d1, left_on="emp",right_on="name"))

print('!'*50)
d=p.DataFrame({'emp':['bob','bilal','yassen','lisa'],'group':['sql','data','php','desgin']})

d1=p.DataFrame({'name':['bilal','bob','yassen','lisa'],'date':[1999,1988,2001,2004]})
print(d)
print(d1)

print(p.merge(d,d1, left_on="emp",right_on="name").drop('name',axis=1))

print('!'*50)
d=p.DataFrame({'emp':['bob','bilal','yassen','lisa'],'group':['sql','data','php','desgin']})

d1=p.DataFrame({'name':['bilal','bob','yassen','lisa'],'date':[1999,1988,2001,2004]})
print("here")
print(d)
d1=d.set_index('emp')
print(d1)

print('!'*50)

d=p.DataFrame({'a':np.random.rand(10),'b':np.random.rand(10)})
print(d)
print('.'*25)
print(d.sum())
print(d['a'].sum())
print('.'*25)

print(d.prod())#ضرب كل العناصر
print('.'*25)

print(d.mean())
print('.'*25)
print(d.mean(axis='columns'))#صف صف
print('.'*25)
print(d.describe())

print('!'*50)
d=p.DataFrame({'key':['a','b','c','a','b','c'],'data':range(6)},columns=['key','data'])
print(d)
print('.'*25)
print(d.describe())
print('.'*25)
print(d.groupby('key').sum())#مهمة
print('.'*25)
print(d.groupby('key').sum().describe())#مهمة
print('.'*25)

print('!'*50)

d=p.DataFrame({'key':['a','b','c','a','b','c'],'data':range(6),'data1':np.random.randint(0,10,6)})
print(d)
d1=d.groupby('key').aggregate({'data':'min','data1':'max'})#نختار تاقيمة الصغرة والكبرى في الجدول الجديد
print(d1)
print('.'*25)
d1=d.groupby('key').aggregate({'data':'mean','data1':'max'})
print(d1)

print('!'*50)
d=p.DataFrame({'key':['a','b','c','a','b','c'],'data':range(6),'data1':np.random.randint(0,10,6)})
print(d)
def ff(x):
    return x['data1'].mean()>4
d1=d.groupby('key').filter(ff)
print(d1)
d2=d.groupby('key').transform(lambda x:x**2)
print(d2)






