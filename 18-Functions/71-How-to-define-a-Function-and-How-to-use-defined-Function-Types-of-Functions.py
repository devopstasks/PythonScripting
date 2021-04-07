'''
===========================
Function:
=> A function is a block of code for somespecific operation
   Function code is re-usable
   It will execute only when it is called
Why functions are used?
=> Code re-usability
   Improve modularity
Rules to define a function name:
=> Function name should have only A-Z,a-z,_
   Function should not start with number but can be start with _
   Don't include any spaces in between the function name
   Function must be defined before calling it
Types of functions
=> Basically, functions are of two types
   Built-in functions:
   -> Functions that are built into python.
   User-Defined functions:
   -> Functions defined by the users themselves.
===========================
'''
#display() #cannot call before defining the function
def display():
    print("welcome to function concepts")
    print("Simple way to define your function")
    return None
display()
#Below are usage of built-in functions
x="hello"
print(len(x))
y=(5,6)
print(len(y))
print(min(y))
print(max(y))
