'''
=======================================
Practice with subprocess module
=> Find bash version of linux os module
=> Find java version in linux os
=======================================
'''
'''
import subprocess
cmd=['bash','--version']
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
if rc==0:
    for each_line in o.splitlines():
        if "version" in each_line and "release" in each_line:
            print(each_line.split()[3].split('(')[0])
else:
    print("command was failed and error is: ",e)
'''
'''
#Note: java -version prints to stderr instead of stdout
import subprocess
cmd=["java","-version"]
sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
o,e=sp.communicate()
if rc==0:
    if bool(o)==True:
        print(o)
    if bool(o)==False and bool(e)==True:
        print(e.splitlines()[0].split()[2].strip('\"'))
else:
    print("command was failed and error is: ",e)

'''
