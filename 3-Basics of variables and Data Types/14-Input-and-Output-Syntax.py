'''
#Simple arithmetic operation
a=4
b=4
result=a+b
print(f"The addition of {a} and {b} is: {result}")
'''
a=input("Enter a value:")
b=input("Enter b value:")
print(f"The addition of {a} and {b} is: {a+b}")

'''
================================
>>> a=input("Enter a value:")
Enter a value:10
>>> b=input("Enter b value:")
Enter b value:20
>>> print(f"The addition of {a} and {b} is: {a+b}")
The addition of 10 and 20 is: 1020
>>> print(f"The addition of {a} and {b} is: {eval(a)+eval(b)}")
The addition of 10 and 20 is: 30
>>>
=================================
'''
'''
=================================
We should read the inputs as below:
a=eval(input("Enter a value:"))
b=eval(input("Enter b value:"))
print(f"The addition of {a} and {b} is: {a+b}")
==================================
'''
