import numpy as np
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
row_r1 = a[1, :]    # Rank 1 view of the second row of a
row_r2 = a[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"


#a = np.zeros((4,4))   # Create an array of all zeros
#print(a[2,2])
#from random import randint
#print(randint(0, 9))

#e = np.random.random((2,2))  # Create an array filled with random values
