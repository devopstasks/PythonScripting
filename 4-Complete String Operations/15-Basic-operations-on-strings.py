'''
===================
Creatting string
-use '',"" or """ """(for multiple lines)
====================
my_name="Sunil"
my_new_name="python developer"
my_info="""
I started my career as a java developer
and moved to devops team.
"""
print(f"my_name is: {my_name} \nmy_new_nameis: {my_new_name} \nmy_info is: {my_info}")
'''
'''
my_str=""
print(f"{bool(my_str)}")
my_str=" "
print(f"{bool(my_str)}")
'''

'''
========================
Note: strings are immutable. we cannot change part of a string, however we can re-assign or delete a string.
========================
my_fav_scripting="python scripting"
print(my_fav_scripting)
print(my_fav_scripting[0])
print(my_fav_scripting[15])
#print(my_fav_scripting[16])
print(my_fav_scripting[-1])
print(my_fav_scripting[-2])
print(my_fav_scripting[0:6])#This prints 6 characters starting from 0th index
print(my_fav_scripting[0:])#This prints all the characters.This is called slicing the string
str1="hello"
str1[3]="k"
'''
'''
================================
Length of a string: use len function
===================================
lenth_of_str="sample string"
print(f"string is \"{lenth_of_str}\" and it's length is {len(lenth_of_str)}")
'''
'''
========================================
Concatenating strings
========================================
str1="python"
str2="scripting"
print(str1+" "+str2)
print(str1+" "+str2+" "+"tutorials")
'''
