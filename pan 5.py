import pandas as p
import numpy as np

d=p.DataFrame(np.random.rand(3,2),columns=['food','drink'],index=['a','b','c'])
print(d)

print("!"*20)
w=p.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
x=p.Series({'a':6,'b':7,'c':8,'d':9,'e':10})
y=p.Series({'a':11,'b':12,'c':13,'d':14,'e':15})
z=p.Series({'a':17,'b':18,'c':19,'d':20,'e':16})
g=p.DataFrame({'math':w,'php':x,'sql':y,'html':z})
g['total']=(g['math']+g['html']+g['sql']+g['php'])/100
print(g)

print("!"*20)
d=p.DataFrame(np.random.rand(5,3),columns=['a','b','c'])
r=(d['a'] +d['b'] /d['c'])
print(d)
print(r)
r=p.eval("(d.a+d.b)/(d.c-1)")
print(r)
r=d.query('a < 0.5 and b > 0.5')
print(r)
#مهم
tmp1=d.a<0.5
tmp=d.b<0.5
tem3=tmp & tmp1
r=d[tem3]
print(d)
print(r)

r=d.query('a < 0.5 or b < 0.5')
print(r)

print("!"*50)
def m(cols,ind):
    d={c:[str(c)+str(i)for i in ind]for c in cols}
    return p.DataFrame(d,ind)
print(m("abcd",range(3)))








