'''
===============================
Simple function with arguments
===============================
'''
'''
a=eval(input("Enter your first number: "))
b=eval(input("Enter your second number: "))
result=a+b
print(f'The addition of {a} and {b} is: {result}')
'''
def get_add(num1,num2): # Here num1 and num2 are called parameters or positional arguments
    aresult=num1+num2
    print(f'The addition of {num1} and {num2} is: {aresult}')
    return None
def get_sub(num1,num2):
    sresult=num1-num2
    print(f'The substraction of {num1} and {num2} is: {sresult}')
    return None
def main():
    #a=eval(input("Enter your first number: "))
    #b=eval(input("Enter your second number: "))
    #get_add(a,b) # Here a and b are called arguments
    #get_sub(a,b)
    get_add(5,4)
    get_sub(5,4)
    return None
main()
