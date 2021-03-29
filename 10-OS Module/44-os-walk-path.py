'''
==================================
os.walk(path)
=> Used to generate directory and file names in a directory tree by walking
   Note: First complete for loop then start this os.walk

Ex:
find path -name *.txt
/home/xyz
/home/xyz/dir1
/home/xyz/dir1/sub1
==================================
'''

'''
import os
path="C:\\Users\\Automation\\Desktop\\new\\mydir\\scripting"
print(os.walk(path))
print(list(os.walk(path)))
'''

'''
import os
path="C:\\Users\\Automation\\Desktop\\new\\mydir\\scripting"
print("-----------------------")
for each in os.walk(path):
    print each
'''

'''
import os
path="C:\\Users\\Automation\\Desktop\\new\\mydir\\scripting"
print("-----------------------")
for r,d,f in os.walk(path):
    print(r)    #prints only path
    print(r,f)  #prints only path and files
    print(r,d)  #prints only path and directory
'''

'''
import os
path="C:\\Users\\Automation\\Desktop\\new\\mydir\\scripting"
print("-----------------------")
for r,d,f in os.walk(path,topdown=False):   #Here we are reversing the output from bottom to top
    print(r,f)  #prints only path and files
'''

'''
#print the path if it has files
import os
path="C:\\Users\\Automation\\Desktop\\new\\mydir\\scripting"
print("-----------------------")
for r,d,f in os.walk(path):
    if len(f) != 0:
        print(r,f)
'''

'''
#print the path and list the files
import os
path="C:\\Users\\Automation\\Desktop\\new\\mydir\\scripting"
print("-----------------------")
for r,d,f in os.walk(path):
    if len(f) != 0:
        print(r)
        for each_file in f:
            print(each_file)
'''

'''
#print the path and files with complete paths
import os
path="C:\\Users\\Automation\\Desktop\\new\\mydir\\scripting"
print("-----------------------")
for r,d,f in os.walk(path):
    if len(f) != 0:
        print(r)
        for each_file in f:
            print(os.path.join(r,each_file))
        print("-----------------------")
'''
