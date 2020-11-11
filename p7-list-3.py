a = 1
t1 = ["apple1", "banana1", "cherry1"]
for x in range(0,3,1):
    a = a + 1
    t1.append ("xyz" + str (a)) 
    if (x==3): 
         break
print (t1)
t1.insert(2, "mmm")
print (t1)
    