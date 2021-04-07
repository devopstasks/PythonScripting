'''
==================================
compile operation of re module
=> If we have to use the same pattern in multiple places in the script, we compile the pattern into an object
   This executes faster
   re.findall(my_pat,text) ===> re.compile(my_pat).findall(text)
==================================
'''
import re
text="This is about python. Python is easy to learn and we have two major versions: python2 and python3"
my_pat=r'\bPython[23]?\b'
'''
print(re.search(my_pat,text))
print(re.findall(my_pat,text,flags=re.I))
print(re.split(my_pat,text,flags=re.I))
#output -
<re.Match object; span=(22, 28), match='Python'>
['python', 'Python', 'python2', 'python3']
['This is about ', '. ', ' is easy to learn and we have two major versions: ', ' and ', '']
'''
'''
pat_obj=re.compile(my_pat,flags=re.I)
print(pat_obj)
print(pat_obj.search(text))
print(pat_obj.findall(text))
#output -
re.compile('\\bPython[23]?\\b', re.IGNORECASE)
<re.Match object; span=(14, 20), match='python'>
['python', 'Python', 'python2', 'python3']
'''
