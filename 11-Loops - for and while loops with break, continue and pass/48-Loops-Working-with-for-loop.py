'''
=============
Loops
=> Execute a block of code many times
=> Python has 2 types of Loops
   - for loop
   - while loop
=> for loop is used to iterate over a sequence(list, tuple, string) or other iterable objects
=============
'''
'''
# Iterate over a list
for x in [4,5,6]:
    print(x)
'''
'''
# Iterate over a tuple
for value in (4,5,6,'Hi'):
    print(value)
'''
'''
# Iterate over a string
for each_char in "python":
    print(each_char)
'''

num_list=[3,2,7,4,8,5,10]
for each in num_list:
    if (each%2)==0:
        print(f'{each} is even')
    else:
        print(f'{each} is odd')
