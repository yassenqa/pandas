import pandas as p 

d=p.read_csv("C:/Users/SEB/Desktop/course 2/iris.csv")
d1=p.read_excel("C:/Users/SEB/Desktop/course 2/1.xls")
print(d.head(20))# عرض الملف #وعدد الاسطر
print('.'*25)

import pandas as p 
d=p.read_csv("C:/Users/SEB/Desktop/course 2/iris.csv",index_col='sepal.length')
print(d.head(20))
print('.'*25)


w=p.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
x=p.Series({'a':6,'b':7,'c':8,'d':9,'e':10})
y=p.Series({'a':11,'b':12,'c':13,'d':14,'e':15})
z=p.Series({'a':17,'b':18,'c':19,'d':20,'e':16})
g=p.DataFrame({'math':w,'php':x,'sql':y,'html':z})
print(w)
print(g)
#g.to_csv("C:/Users/SEB/Desktop/course 2/grads.csv")# حفظ ملف
print(g.head())

print('.'*25)


w=p.Series({'a':1,'b':2,'c':3,'d':4,'e':5})
x=p.Series({'a':6,'b':7,'c':8,'d':9,'e':10})
y=p.Series({'a':11,'b':12,'c':13,'d':14,'e':15})
z=p.Series({'a':17,'b':18,'c':19,'d':20,'e':16})
g=p.DataFrame({'math':w,'php':x,'sql':y,'html':z})

print(g)
#g.to_excel("C:/Users/SEB/Desktop/course 2/1.xls",sheet_name='eee')

print('.'*25)
print(d1)

#d3=d.to_excel("C:/Users/SEB/Desktop/course 2/2.xls",sheet_name='from csv')

print('.'*25)
names=['a','b','c','d','e']
x=p.read_csv("C:/Users/SEB/Desktop/course 2/iris.csv",names=names)
print(x)







