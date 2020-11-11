import matplotlib.pyplot as plt 
plt.bar([1,3,5,7,9],[5,4,7,8,3], label = 'first exp')
plt.bar([7,8,5,5,3], [3,4,3,6,5], label = '2nd  exp', color = 'g')

plt.title ("title")
plt.xlabel ("X")
plt.ylabel ("Y")
plt.legend()
plt.grid (True,color ='k')
plt.show ()

