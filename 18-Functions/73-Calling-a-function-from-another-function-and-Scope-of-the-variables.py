'''
======================
Scope of the variable
======================
'''
def myfunction1():
    x=20 #This is Local variable
    print("Inside myfunction1")
    print("value of x:",x)
    return None
def myfunction2():
    #x=30
    print("Inside myfunction2")
    print("value of x:",x)
    return None
#myfunction1()
x=40 #This is Global variable
#myfunction2()
def main():
    #global x # This is how to make a variable global, but not a good idea
    #x=100
    myfunction1()
    myfunction2()
    return None
main()
