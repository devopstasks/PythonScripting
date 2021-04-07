'''
====================
Rules to create a pattern- Part2
^ => Start of the string(and start of the line in-case of multiline string)
$ => End of the string(and newline character in-case of multiline string)
\b => Empty string at the begining or end of a word
\B => Empty string not at the begining or end of a word
\t,\n,\r => Matches tab,newline,return respectively

my_pat=r"\blearn\b"
Note: Here r stands for raw-string and by using this, special characters are skipped.
====================
'''
'''
import re
text="it is a python and it is easy to learn"
my_pat='i[ts]' #output- ['it', 'is', 'it', 'is']
print(re.findall(my_pat,text))

my_pat='^i[ts]' #output- ['it']
print(re.findall(my_pat,text))

'''
import re
text="isa python andlearn it learn is easy to learn"
#my_pat="learn" #output- ['learn', 'learn', 'learn']
#my_pat="learn$" #output- ['learn']
#my_pat="learn\b" #output- [] here only \b is considered as backspace
#my_pat="learn\\b" #output- ['learn', 'learn', 'learn']
#my_pat="\\blearn" #output- ['learn', 'learn']
#my_pat=r"\blearn\b" #output- ['learn', 'learn']
#my_pat=r"\Blearn\B" #output- []
my_pat=r"\t" #output- []
print(re.findall(my_pat,text))
