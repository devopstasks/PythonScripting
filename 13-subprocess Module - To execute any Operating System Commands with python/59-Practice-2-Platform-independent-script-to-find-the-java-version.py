'''
===========================
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
===========================
'''
