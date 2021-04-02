'''
======================
subprocess module
=> Used to execute operation system commands
import subprocess
sp=subprocess.Popen(cmd,shell=True/False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f'OUTPUT is: {out}')
print(f'ERROR is: {err}')

if shell=True, then your cmd is a string (as your os commands)
if shell=False, then your cmd is a list
Note:-
shell=False donot work on your os environment variables
Ex:
  shell=True  ==> cmd="ls -lrt"
  shell=False ==> cmd="ls -lrt".split() or ['ls','-lrt']

Note:-
shell=True always on windows and cmd is a string
======================
'''
import subprocess
cmd="dir"
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)
rc=sp.wait()
out,err=sp.communicate()
print(f'The return code: {rc}')
print(f'OUTPUT is: {out}')
print(f'ERROR is: {err}')
