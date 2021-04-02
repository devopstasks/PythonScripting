'''
==========================
Read a directory path and identify all files and directory
==========================
'''
'''
#Sample for loop
for each in [2,3,4,5]:
    print("hello",each)
'''

import os
import sys
path=input("Enter your path: ")
if os.path.exists(path):
    df_l=os.listdir(path)
else:
    print("please provide a valid path")
    sys.exit()

list_of_files_dir=os.listdir(path)
print("all files and dir: ",list_of_files_dir)
for each_file_or_dir in list_of_files_dir:
    f_d_p=os.path.join(path,each_file_or_dir)
    if os.path.isfile(f_d_p):
        print(f'{f_d_p} is a file')
    else:
        print(f'{f_d_p} is a directory')
