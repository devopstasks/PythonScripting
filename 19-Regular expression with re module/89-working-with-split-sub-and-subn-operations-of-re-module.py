'''
=====================================
split and sub,subn operationsof re module
help(re.split())
help(re.sub())
help(re.subn())
=====================================
'''
import re
text="This is about python and python is very easy and we are having python2 vers and Python3 vers"
my_pat=r'python[23]?'
#print(re.split(my_pat,text,flags=re.I))
#output - ['This is about ', ' and ', ' is very easy and we are having ', ' vers and ', ' vers']

print(re.sub(my_pat,"jython",text))
#output - This is about jython and jython is very easy and we are having jython vers and Python3 vers
print(re.sub(my_pat,"jython",text,flags=re.I))
#output - This is about jython and jython is very easy and we are having jython vers and jython vers
print(re.sub(my_pat,"jython",text,count=1,flags=re.I))
#output - This is about jython and python is very easy and we are having python2 vers and Python3 vers

print(re.subn(my_pat,"jython",text,flags=re.I))
#output - ('This is about jython and jython is very easy and we are having jython vers and jython vers', 4)
print(re.subn(my_pat,"jython",text,count=1,flags=re.I))
#output - ('This is about jython and python is very easy and we are having python2 vers and Python3 vers', 1)
