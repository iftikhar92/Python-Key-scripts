class cs1:
    def __init__(self, cycolor, cybrand, cymodel): 
        self.cycolor = cycolor
        self.cybrand = cybrand
        self.cymodel = cymodel
obj1 = cs1("blue", "China" , 2018)
print(obj1.cycolor)
print(obj1.cybrand)
print(obj1.cymodel)
print ("object properties")
obj2 = cs1("black", "China" , 2017)
print(obj2.cycolor)
print(obj2.cybrand)
print(obj2.cymodel)
obj3= obj2 
print ("Object3")
print(obj2.cycolor)

