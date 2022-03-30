from pandas import *
data=Series([0.25,0.5,0.75,1.0],[23,22,21,10])#idتقوم بجعلهم كجدول الليست الثانية هي ال 

print(data)
print("!"*50)
print(data.index)
print("#"*50)
print(data.keys)
print("#"*50)
data=Series((3,6,9,8,5,2,2,6,2,5,8))#22235566889
print(data.describe())#ALL data احتمالات 
print(data.agg(['max','min']))#singl او لتحديد اي وجدة من الاحتمالات
print("#"*50)#دون ترتيب
print(data[1])
print(data[1:3])#الايندكس +فاليو
print(data[1:4:2])

print("*"*50)

data2=Series({'a':1,'b':2,'c':3,'d':4})
print(data2)



x=Index([2,3,5,7,11])#poteto
print(x)

b=Index([4,3,6,7,2])
print(x)
print(b)
print(b & x)#تشابه
print(b ^ x)#لفرق
print(x | b)#اجتماع