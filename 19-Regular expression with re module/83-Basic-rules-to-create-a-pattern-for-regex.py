'''
=======================================
Python Regular expressions
=> Rules to create a pattern
=======================================
'''
'''
The regex is a procedure in any language to look for a specified pattern in a given text
re is the module to perform regex in Python.(use import re in scripts)
There are different operations in re like:
    -> search,match,finditer,findall,split,sub etc..
Syntax:
-> re.search(pattern,text)
-> re.match(pattern,text)
-> re.finditer(pattern,text)
-> re.findall(pattern,text)

Pattern is a sequence of characters, which represent multiple strings
Simple example for pattern:
    => "Python"
    => "Python[23]" -> "Python2", "Python3"
    => r"Python" or r"Python[23]"
'''
'''
=======================
Learning pattern creation with findall operation
How to use findall
========================
import re
text="This is python and it is easy to learn"
my_pattern="is"
print(re.findall(my_pattern,text))
print("no of matches: ",len(re.findall(my_pattern,text)))
'''

'''
===============================
Rules to create a pattern
a,X,9 => Ordinary characters that match themselves
[abc] => Matches a or b or c
[a-c] => Matches a or b or c
[a-zA-Z0-9] => Matches any letter from (a to z) or (A to Z) or (0 to 9)
\w => Matches any single letter, digit or underscore
\W => Matches any character not part of \w
\d => Matches decimal digit 0-9
.  => Matches any single character except newline character

Note: Use \. to match .
===============================
'''
'''
import re
text="This is. a python9 and it @ is easy -to _ learn_@"

my_pat="[a-d]"
print(re.findall(my_pat,text))

my_pat="\w\w\w"
print(re.findall(my_pat,text))

my_pat="\w"
print(re.findall(my_pat,text))

my_pat="\W"
print(re.findall(my_pat,text))

my_pat="python\d"
print(re.findall(my_pat,text))

my_pat="..."
print(re.findall(my_pat,text))

my_pat="\." # This matches . with .
print(re.findall(my_pat,text))
'''
import re
text="This is my ip of a db server: 255.100.102.103"
#my_pat="\d\d\d"
#my_pat="\d\d\d.\d\d\d.\d\d\d.\d\d\d"
my_pat="\d\d\d\.\d\d\d\.\d\d\d\.\d\d\d" #This matches . with . only
print(re.findall(my_pat,text))
