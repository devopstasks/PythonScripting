'''
=========================================
Functions with arguments and return value
==========================================
'''
def get_add(num1,num2):
    result=num1+num2
    return result
def get_sub(num1,num2):
    result=num1-num2
    return result
def main():
    #a=eval(input("Enter your first number: "))
    #b=eval(input("Enter your second number: "))
    #aresult=get_add(a,b)
    #sresult=get_sub(a,b)
    a,b=5,4
    aresult=get_add(a,b)
    sresult=get_sub(a,b)
    print(f'The addition of {a} and {b} is: {aresult}')
    print(f'The substraction of {a} and {b} is: {sresult}')
    return None
main()
