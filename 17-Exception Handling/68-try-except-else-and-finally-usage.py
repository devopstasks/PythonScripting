'''
==============================================================
Difference between 'try except finally' and 'try except else'
=> else block executes if there is no exceptions in try block
=> finally block always executes
==============================================================
'''
try:
    a=9
    print(a)
except NameError:
    print("Variable is not defined")
except Exception as e:
    print("Exception occured: ",e)
else:
    print("This will execute if there is no exceptions in try block")
finally:
    print("This will executes finally")
