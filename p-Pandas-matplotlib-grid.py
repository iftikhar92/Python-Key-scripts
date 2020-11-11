import matplotlib.pyplot as plt
#import pandas as pd
#df = pd.read_csv('export.csv')
#print (df['a'])
#plt.hist( df['a'] , df['b'])

from matplotlib import style
style.use('ggplot')
x =  [5,8,10]
y = [12,16,6]
x2 = [6,9,11]
y2 = [6,15,7]
plt.plot(x,y,'g',label ='line one', linewidth=5)

plt.plot(x2,y2,'c',label ='line two', linewidth=5)

plt.title ("title 1")
plt.xlabel ("X")
plt.ylabel ("Y")
plt.legend()
plt.grid (True,color ='k')
plt.show ()

