import pandas as pd
from numpy.random import randn
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from pandas import DataFrame, Series

#Plotting subplots
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
#plt.show()

ax1.set_title('Histogram')
ax2.set_title('Scatter plot')
ax3.set_title('Bar plot')
ax4.set_title('Line plot')
plt.plot(randn(50).cumsum(),'ko--')  #cumulative sum
ax1.hist(randn(100),bins=20,color='b',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))
ax3.barh(np.arange(5),color='g',width=0.6,height=0.8)
#plt.show()

fig1= plt.figure()
data = randn(30).cumsum()
plt.title('Step plot')
plt.plot(data, 'k--', label='Default')
plt.plot(data, 'b--', drawstyle='steps-post', label='step-post')
plt.legend(loc='best')
#plt.show()


#Line plot
df = DataFrame(np.random.randn(10,4).cumsum(0),columns=['A','B','C','D'],index=np.arange(0,100,10))
df.plot()
#plt.show()

#Bar plot
fig2,axes= plt.subplots(2, 1)
data1= Series(np.random.randn(16),index=list('abcdefghijklmnop'))
data1.plot(kind='bar',ax=axes[0],color='b',alpha=0.7)
data1.plot(kind='barh',ax=axes[1],color='g',alpha=0.7)
plt.show()