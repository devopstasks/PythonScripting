'''
===================================
Print the method names of Dictionary: print(dir({}))
python2: Dictionary is un-ordered
python3: Dictionary is ordered
===================================
my_dict={}
print(my_dict,type(my_dict))
print(bool(my_dict))
'''
'''
my_dict={"fruit":"apple","animal":"tiger",3:"abc","hhh":8}
print(my_dict)
print(my_dict["animal"])
print(my_dict.get(3))
#print(my_dict["ppp"])
print(my_dict.get("ppp"))
print(dir({}))
print(my_dict)
my_dict.clear()
print(my_dict)
'''
'''
my_dict={"fruit":"apple","animal":"tiger",3:"abc","hhh":8}
my_dict["three"]=3
print(my_dict)
my_dict["three"]=66
print(my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict=my_dict
print(id(my_dict),id(my_new_dict))
x=my_dict.copy()
print(id(x))
'''
'''
my_dict={"fruit":"apple","animal":"tiger",3:"abc","hhh":8}
print(my_dict)
my_new_dict={"four":4}
my_dict.update(my_new_dict)
print(my_dict)

my_dict.pop("hhh")
print(my_dict)
remove_item=my_dict.popitem()
print(remove_item)
print(my_dict)
'''
'''
my_keys=['a','e','i','o','u']
new_dict=dict.fromkeys(my_keys)
print(new_dict)
new_dict['a']="hello"
print(new_dict)
'''
