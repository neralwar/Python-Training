import pandas as pd
 
import matplotlib.pyplot as plt
 
from matplotlib import style
 
style.use('fivethirtyeight')
 
customerdata= pd.read_excel('Test.xlsx',sheet_name='Sheet1')

time = [0, 1, 2, 3]
position = [0, 100, 200, 300]

plt.plot(time, position)
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')

plt.show()

import numpy as np 
a = np.arange(0,60,5) 
b=np.arrange(0,100,1)

plt.plot(a,b)

plt.show()


print(a)




