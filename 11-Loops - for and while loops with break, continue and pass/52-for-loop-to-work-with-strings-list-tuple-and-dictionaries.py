'''
===================
=> for loop for string,list,tuple and dictionaries
===================
'''
'''
my_string="working with for loop"
for each_char in my_string:
    print(each_char)
print(" ".join(my_string))
print("\n".join(my_string))
'''
'''
my_list=[1,2,3,4,5]
for each_value in my_list:
    print(each_value)
'''
'''
my_list=[(1,2),(3,4),(5,6)]
for each_item in my_list:
    print(each_item)
for f,s in my_list: # This is example of unpacking variables
    print(f,s)
'''
'''
my_list=[[1,2],[3,4],[5,6]]
for f,s in my_list: # This is example of unpacking variables
    print(f,s)
'''
my_dict={"a":1,"b":2,"c":3}
for each in my_dict:
    print(each)
for each in my_dict.keys():
    print(each)
for each in my_dict.values():
    print(each)
for each in my_dict.items():
    print(each)
for key,value in my_dict.items(): # This is example of unpacking variables
    print(key,value)
