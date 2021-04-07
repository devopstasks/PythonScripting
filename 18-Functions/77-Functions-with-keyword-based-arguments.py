'''
===================================
Functions with keyword-based arguments
===================================
'''
def display(a,b):
    print(f'a={a}')
    return None
display(3,4)
display(a=3,b=4)
display(b=4,a=3) # Here we are explicitly assigning values to variables
