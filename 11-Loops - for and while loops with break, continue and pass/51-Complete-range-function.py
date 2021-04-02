'''
===================
Python range() function
=> It is a built-in function
=> Generates integers as a list
=> Syntax:
   range(start,stop,step)
   3-argument => By default start=0, step=1
===================
'''
'''
print(list(range(5)))
print(list(range(0,5)))
print(list(range(0,5,1)))

print(list(range(10,2))) #This prints empty list
print(list(range(10,2,-1))) # This prints in reverse order
'''
'''
for each in range(5):
    print(each)
'''
my_list=[2,4,5,7,"python"]
print(range(len(my_list)))
print(list(range(len(my_list))))
for each_index in range(len(my_list)):
    print(f'Index-->{each_index} value: {my_list[each_index]}')
