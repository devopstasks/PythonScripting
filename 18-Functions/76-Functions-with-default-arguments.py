'''
===============================
Functions with default arguments
===============================
'''
'''
def display(a):
    print("The value of a is: ",a)
    return None
display(4)
display(5)
display()
'''
'''
def display(a=1): # This is how default argument is defined
    print("The value of a is: ",a)
    return None
display(4)
display(5)
display()
'''
'''
def add_numbers(a,b):
    result=a+b
    print("The result is: ",result)
    return None
add_numbers(4,5)
add_numbers(5)
'''
'''
def add_numbers(a=0,b): # SyntaxError: non-default argument follows default argument
    result=a+b
    print("The result is: ",result)
    return None
add_numbers(4,5)
add_numbers(5)
'''
'''
def add_numbers(a,b=0): # Define the default argument at last
    result=a+b
    print("The result is: ",result)
    return None
add_numbers(4,5)
add_numbers(5)
'''

def working_on_some(user="root"):
    print(f'working with {user}')
    return None
working_on_some("weblogic_admin")
