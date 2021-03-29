'''
=================================================
os module
=> This module is used to work/interact with operating system to automate many
   more tasks like- creating directory, removing directory, identifying current directory and many more,

Operations of os module:
=> Four parts of os:
   os
   os.path
   os.system()
   os.walk()

=> Simple os Operations
   os.sep
   os.getcwd()
   os.chdir(path)
   os.listdir()
   os.listdir(path)
   os.mkdir(path)
   os.makedirs(path) -> (Recursive directory creation function)
   os.remove()
   os.removedirs(path) -> (Remove directories recursively)
   os.rmdir(path)
   os.rename(src,dest)
   os.environ
   os.getuid()
   os.getpid()
=================================================
'''
import os
print(os.sep)
print(os.getcwd())
print(os.listdir())
print(os.environ)
print(os.getuid())
print(os.getpid())
