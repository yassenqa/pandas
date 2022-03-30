import pandas as p
import numpy as np
#   m   p   s   h
#a                  
#b                  
#c                  
#d
#e
#


w=p.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
x=p.Series({'a':6,'b':7,'c':8,'d':9,'e':10})
y=p.Series({'a':11,'b':12,'c':13,'d':14,'e':15})
z=p.Series({'a':17,'b':18,'c':19,'d':20,'e':16})
g=p.DataFrame({'math':w,'php':x,'sql':y,'html':z})
print(g.loc[g.math>3])
print(g.iloc[3,2])

print(g.loc[g.math>3,['php','math']])

print(g.index)
print (g.columns)

print(g['math'])

print(g.sort_values(['math'],ascending=False))#ترتيب تنازلي
print(g.sort_values(['html'],ascending=True))#ترتيب تصاعدي

print(g.max())#للكل
print(g.min())#للكل
print(g.mean())#للكل
print(g.std())#للكل

print(g['math'].max())
print(g['math'].min())
print(g['math'].mean())
print(g['math'].std())

print('!'*50)
d=p.DataFrame(np.random.rand(5,3),columns=['a','b','c'])
print(d)
print(d.corr())#بيعطيني علاقة ارتباط الاعمدة مع بعضها
print(d.skew())#مدى انحراف الارقام عن بعضها

print('!'*50)
data=[{'square':i**2,'cube':i**3,'root':i**0.5} for i in range(10)]
d=p.DataFrame(data)
print(d)
print('!'*50)
d=p.DataFrame([{'a':1,'b':2},{'a':3,'b':4},{'a':6,'b':7}])
print(d)






