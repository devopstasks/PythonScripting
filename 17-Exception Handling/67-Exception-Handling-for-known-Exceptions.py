'''
========================================
Exception handling for known exceptions
========================================
'''
try:
    #print(a)
    #print(4+"hi")
    #open("abc.txt")
    #print(5/0)
    import fabric
except NameError:
    print("Variable is not defined")
except TypeError:
    print("Adding number and string is not possible")
except FileNotFoundError:
    print("File is not present to open it")
except ZeroDivisionError:
    print("Division with zero is not possible")
except ModuleNotFoundError:
    print("Please install fabric module to use it")
except Exception as e:
    print(e)
finally:
    print("This will execute finally")
