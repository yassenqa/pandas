import pandas as p 
import numpy as np 
#MultiIndex
index=[('cal',2000),('cal',2010),('ny',2000),('ny',2010),('tex',2000),('tex',2010)]
pop=[10000,15000,20000,25000,30000,35000]

index=p.MultiIndex.from_tuples(index)

pp=p.Series(pop,index=index)
pp=pp.reindex(index)
print(pp)
print(pp[:,2010])
print(pp.unstack())

ppp=p.DataFrame({'totle':pp,'under18':[456123,25896,14578,321456,45678,88575]})
print(pp)
print(ppp)
ppp=p.DataFrame(np.random.rand(4,2), index=[['a','b','c','d'],[1,2,3,4]],columns=['hi','hello'])
print(ppp)









