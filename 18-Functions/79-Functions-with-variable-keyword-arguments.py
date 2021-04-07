'''
======================================================
Function with variable length keyword-based arguments
=> Here arguments are stored in a dictionary
======================================================
'''
'''
def display(**karg):
    print(karg)
    return None
#display(4,5)
display(b=5,a=4)
display(a=4,b=5,c=6)
display(x=5,y="hi",z=6.7,path="root")
'''
def display(p,**karg): # Here we are specifying both normal and variable keyword-based arguments
    print(p)
    print(karg)
    return None
#display(4,5)
#display(b=5,a=4)
#display(a=4,b=5,c=6)
display(35,x=5,y="hi",z=6.7,path="root")
