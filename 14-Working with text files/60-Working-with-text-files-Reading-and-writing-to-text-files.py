'''
==============================
Working with text files using python
Create a new file
add content to an existing file
read a file content
open --> w
     --> a
     --> r
==============================
'''
'''
#working with text files
fo=open('newdemo.txt','w')
print(fo.mode())
print(fo.readable())
print(fo.writable())
'''
'''
fo=open('random.txt','w')
fo.write("This is a first line\n")
fo.write("This is a second line\n")
fo.write("This is a third line")
fo.close()
'''
'''
my_content=["This is dataset-1\n","This is dataset-2\n","This is dataset-3"]
fo=open('random.txt','w')
fo.writelines(my_content)
fo.close()
'''
'''
my_content=["from loop-iteration-1","from loop-iteration-2","from loop-iteration-3"]
fo=open('random.txt','w')
for each_line in my_content:
    fo.write(each_line+"\n")
fo.close()
'''
'''
fo=open('random.txt','r')
data=fo.read()
fo.close()
print(data)
'''
fo=open('random.txt','r')
data=fo.readlines()
fo.close()
print(data)
for each_line in data:
    print(each_line)
print("-----------")
#Print only last line
print(data[-1])
