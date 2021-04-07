'''
==========================================================
1) How to use functions of one python script into another python script?
2) What is __name__ variable?
3) How to create user defined modules?
==========================================================
'''
'''
1) How to use functions of one python script into another python script?
'''
#script1.py
#
def add(a,b):
    print(f'The addition of {a} and {b} is: {a+b}')
    return None
def sub(a,b):
    print(f'The substraction of {a} and {b} is: {a-b}')
    return None
def main():
    x=12
    y=32
    add(x,y)
    sub(x,y)
# This ensures main() of this script is only called if this script is executed.
if __name__ == "__main__":
    main()

#script2.py
#
import script1
def mul(a,b):
    print(f'The multiplication of {a} and {b} is: {a*b}')
    return None
def main():
    x=10
    y=20
    mul(x,y)
    script1.add(x,y)
    script1.sub(x,y)
# This ensures main() of this script is only called if this script is executed.
if __name__ == "__main__":
    main()


'''
3) How to create user defined modules?
=> New Structure to create python script
=> We follow the below structure to create our own module.
'''
import sys
import os
import time
import datetime
def addition(a,b):
    print(f'The addition of {a} and {b} is: {a+b}')
    return None
def main():
    x=6
    y=7
    addition(x,y)
    return None
if __name__ == "__main__": # By doing this, we avoid execution of the main() while importing this script into some other script.
    main()
