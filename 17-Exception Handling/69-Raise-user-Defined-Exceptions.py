'''
========================================
Creating Custom Exceptions using:
=> raise  - Used to raise an existing exceptions
=> assert - Used to create an AssertionError
========================================
'''
'''
age=17
if age>=18:
    print("Valid Age")
else:
    raise ValueError("Age is below 18 yrs")
'''
'''
assert 4<3
'''
age=17
try:
    assert age>=18
    print("Valid Age")
except AssertionError:
    print("Raised with assert because age is less than 18")
except Exception as e:
    print("Exception occured: ",e)
