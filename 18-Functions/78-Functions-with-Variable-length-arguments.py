'''
========================================
Functions with variable length arguments
=> Here number of arguments is not fixed.
=> Here arguments are stored in a tuple
========================================
'''
'''
def display(*arg):
    print(arg)
    return None
display()
display(4)
display(4,5)
'''
def display(*arg):
    print(arg)
    for each in arg:
        print(type(each))
    return None
display(2,7)
print("-------------------")
display(3,"hi",8.6)
