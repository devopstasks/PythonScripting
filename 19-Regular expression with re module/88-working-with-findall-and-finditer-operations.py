'''
=========================================
findall and finditer operations of re module
=========================================
'''
import re
text="This is python and we are having python2 and python3 version"
my_pat=r'\bpython[23]?\b'
#print(re.search(my_pat,text))
#print(re.findall(my_pat,text)) #output - ['python', 'python2', 'python3']
for each_obj in re.finditer(my_pat,text):
    print("The match is: ",each_obj.group()," | start index",each_obj.start()," | end index",each_obj.end()-1," | length",each_obj.end()-each_obj.start())
#output:
'''
The match is:  python  | start index 8  | end index 13  | length 6
The match is:  python2  | start index 33  | end index 39  | length 7
The match is:  python3  | start index 45  | end index 51  | length 7
'''
