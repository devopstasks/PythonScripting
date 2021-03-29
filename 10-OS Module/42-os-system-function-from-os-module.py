'''
==================================
os.system() from os module
=> os.system() is used to execute os commands
=> os.system() output can not be stored into a variable
   If command execution sucess, return code is 0
   If command execution fails, return code is non-zero.
==================================
'''
import os
print(os.system("dir"))
print(os.system("mode"))
print(os.system("pwd"))
print(os.system("cls"))

'''
import os
cmd="date"
rt=os.system(cmd)
if rt==0:
    print("your cmd was successfully executed")
else:
    print("your command was failed")
'''
