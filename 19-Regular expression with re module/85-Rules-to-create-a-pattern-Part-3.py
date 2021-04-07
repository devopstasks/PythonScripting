'''
===================================
Rules to create a pattern- Part3
{2} => Exactly 2 times
{2,4} => 2,3 or 4 times
{2,} => 2 or more times
+ => 1 or more
* => 0 or more times
? => once or none(lazy)
==================================
'''
import re
'''
#text="This is a pythonnnn and python"
#text="This is a pythonnnn and python aaa haaaafd aaaaaaaa"
text="This is a pythonnnn and python aaa haaaafd xyzaaaaaaaa"
#my_pat=r'pythonn' #output - ['pythonn']
#my_pat=r'\bpython{4}\b' #output - ['pythonnnn']
#my_pat=r'\ba{8}\b' #output - ['aaaaaaaa']
my_pat=r'\bxyza{8}\b' #output - ['xyzaaaaaaaa']
print(re.findall(my_pat,text))
'''

text="xaz asdfa sdf xaazz xaaaaaaaz xaaaaz xz"
#my_pat=r'\bxaz\b' #output - ['xaz']
#my_pat=r'\bxa{1,4}z\b' #output - ['xaz', 'xaaaaz']
#my_pat=r'\bxa{2,}z\b' #output - ['xaaaaaaaz', 'xaaaaz']
#my_pat=r'xa{1,}z' #output - ['xaz', 'xaaz', 'xaaaaaaaz', 'xaaaaz']
#my_pat=r'xa+z' #output - ['xaz', 'xaaz', 'xaaaaaaaz', 'xaaaaz']
#my_pat=r'xa*z' #output - ['xaz', 'xaaz', 'xaaaaaaaz', 'xaaaaz', 'xz']
my_pat=r'xa?z' #output - ['xaz', 'xz']
print(re.findall(my_pat,text))
