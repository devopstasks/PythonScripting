'''
========================================
Python regular expressions with flags
Rules to create a pattern- Part4

Simple Flags for regex:
Abbreviation    FullName
------------    --------
re.I            re.IGNORECASE
re.M            re.MULTILINE
========================================
'''
'''
import re
text="this is a string  ThIs is a new staring THIS"

my_pat=r'this' #output - ['this']
print(re.findall(my_pat,text))

my_pat=r'this' #output - ['this', 'ThIs', 'THIS']
print(re.findall(my_pat,text,re.I))
'''
import re
text="""this is a string end
this is second line End
This is third line
asfsd this eNd"""
'''
my_pat='^this' #output - ['this']
print(re.findall(my_pat,text))
'''
my_pat='^this' #output - ['this', 'this', 'This']
my_pat='end$' #output - ['end', 'End', 'eNd']
print(re.findall(my_pat,text,re.I|re.M))
