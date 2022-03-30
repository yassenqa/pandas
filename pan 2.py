import pandas as py
import matplotlib.pyplot as plt
data=py.Series((3,6,9,8,5,4,2,6,3,5,8),index=(1,2,3,4,5,6,7,8,9,10,11))
data.plot()

data.plot(kind='line')
plt.show()



