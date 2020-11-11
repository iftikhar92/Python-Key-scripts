def addnum1(x,y): 
    print (x,y) 
    return lambda y : x + y
def main():
    a=3
    b=8
    m = 0 
    m =  addnum1 (a,b)
    print (m)
main()