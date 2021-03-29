'''
===============================
os.path module:
=> os.path is a sub-module of os

os.path operations:
=> os.path.sep
   os.path.basename(path)
   os.path.dirname
   os.path.join(dir1,dir2)
   os.path.split(path) -> is used to split the path name into a pair head and tail
   os.path.getsize(path) -> in bytes
   os.path.exists(path)
   os.path.isfile(path)
   os.path.isdir(path)

===============================
'''
import os
print(os.path.sep)
print(os.getcwd())
path="D:\SAMPLE-PROJECTS\PythonScripting"
print(os.path.dirname(path))
print(os.path.basename(path))
print(os.path.split(path))
print(os.path.exists(path))
print(os.path.isdir(path))
print(os.path.isfile(path))
