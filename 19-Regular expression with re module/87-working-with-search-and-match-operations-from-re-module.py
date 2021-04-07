'''
============================================
search operation from re module
=> It looks throughout the entire string and returns the first match
=> re.search(pattern,string,flags)

match operation from re module
=> It looks only at the starting of a string for a match
=> re.match(pattern,string,flags)
============================================
'''
'''
import re
text="This is for python and there are two major vers python2 and python3 in future python4"
#my_pat=r'\bpython\b' #output - ['python']
my_pat=r'\bpython[23]?\b' #output - ['python', 'python2', 'python3']
#print(re.findall(my_pat,text))
#print(re.search(my_pat,text)) #output - <re.Match object; span=(12, 18), match='python'>
match_obj=re.search(my_pat,text)
#print(match_obj) #output - <re.Match object; span=(12, 18), match='python'>
if match_obj:
    print("match from your pattern: ",match_obj.group()) #output - match from your pattern:  python
    print("starting index: ",match_obj.start())
    print("ending index: ",match_obj.end()-1)
    print("length: ",match_obj.end()-match_obj.start())
else:
    print("No match found")
'''
import re
text="""PYTHON2 This is for python and there are
two major vers python2 and python3 in
future python4"""
my_pat=r'\bpython[23]?\b'
match_obj=re.match(my_pat,text,re.I|re.M)
if match_obj:
    print("match from your pattern: ",match_obj.group()) #output - match from your pattern:  PYTHON2
    print("starting index: ",match_obj.start())
    print("ending index: ",match_obj.end()-1)
    print("length: ",match_obj.end()-match_obj.start())
else:
    print("No match found")
