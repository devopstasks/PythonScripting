'''
====================
Exception Handling
=> A python program terminates as soon as it encounters an error.
Errors are two types:
=> Systax Errors:
   No way to handle syntax errors
=> Runtime Errors:(Exceptions)
   There is a way to handle runtime errors
=> Exceptions can be handled by using try and except block

   try:
       statement-1
       statement-2
       statement-3
       ...
   except:
       print("This is because of something went wrong in try block")
=> Useful:
   try:
       statement-1
       statement-2
       statement-3
       ...
   except Exception as e:
       print("This is because of ",e)
=> Exceptions Examples:
   -> IndexError
   -> ZeroDivisionError
   -> ImportError
   -> ValueError
   -> TypeError
   -> NameError
   -> FileNotFoundError
   -> IOError
====================
'''
'''
print("welcome to exception concept"
print("now it is fine")
'''
'''
print(4/2)
print(4/0)
'''
'''
try:
    print(4/0)
except Exception as e:
    print("The error is: ",e)
'''
'''
try:
    fo=open("abc.txt")
    print(fo.read())
    fo.close()
except Exception as e:
    print("The error is: ",e)
'''
'''
try:
    my_list=[3,4,5]
    print(my_list[0])
    print(my_list[3])
except Exception as e:
    print("The error is: ",e)
print("This code will also executes")
'''
'''
try:
    import fabric
except Exception as e:
    print("Exception occured: ",e)
'''
