'''
==============================
How to copy contents of source file to destination file
==============================
'''
#sfile="D:\\SAMPLE-PROJECTS\\PythonScripting\\random.txt"
#dfile="D:\\SAMPLE-PROJECTS\\PythonScripting\\newrandom.txt"
sfile=input("Enter your source file: ")
dfile=input("Enter your destination file: ")
sfo=open(sfile,'r')
contents=sfo.read()
sfo.close()

dfo=open(dfile,'w')
dfo.write(contents)
dfo.close()
