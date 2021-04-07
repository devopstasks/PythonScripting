'''
=========================
Python Regular Expressions (re module)
What is a Regular Expression (RegEx)?
=> The regex is a procedure in any language to look for a specified pattern in a given text.
=> What is a pattern?
   It is a sequence of characters, which represent multiple strings
   Ex: 'i[st]'      -> is,it
       'python[23]' -> python2,python3
=> The different operations in python re are:
   match()
   search()
   findall()
   finditer()
   sub()
   split()
   compile() etc..
=========================
'''
import re
my_str="python is simple and it easy"
print(re.split("i[st]",my_str))
#output
# ['python ', ' simple and ', ' easy']
