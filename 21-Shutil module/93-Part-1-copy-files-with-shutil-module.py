'''
=======================================
Python Shutil module
=> Python Shutil module provide us a number of high-level operations on files and folders/directories
   like- copy, move, remove and much more.
=> Very useful module for devops while taking backups and database side while copying file with same metadata.
   import shutil
   print(dir(shutil))
=======================================
'''
#copy file(s) with shutil module
import shutil
print(dir(shutil))
#'copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'
src="/home/Automation/working_with_remote_server.py"
dest="/home/Automation/working_with_remote_server.py.bkp"
#copyfile(copy the file but here metadata(permission,timestamp) gets changed)
shutil.copyfile(src,dest)

#copy(copy the file and preserves the permissions,but update the timestamp)
shutil.copy(src,dest)

#copy2(copy the file and preserves the complete metadata(permissions,timestamp))
shutil.copy2(src,dest)

#copymode(copy only the file permissions of src file to dest file)
shutil.copymode(src,dest)

#copystat(copy only the complete metadata(permissions,timestamp) of src file to dest file)
shutil.copystat(src,dest)

#copyfileobj(copy one fileobject into other)
f1=open('xyz.txt','r')
f2=open('abc.txt','w')
shutil.copyfileobj(f1,f2)

#copytree(copy/clone the entire directory structure with metadata of src to dest)
src="/home/Automation/tomcat7"
dest="/tmp/tomcat7"
shutil.copytree(src,dest)

#rmtree(removes the entire tree)
shutil.rmtree("/tmp/tomcat7")
