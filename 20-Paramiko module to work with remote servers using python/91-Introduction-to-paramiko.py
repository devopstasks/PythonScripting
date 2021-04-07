'''
==================================================================================================
Working with remote Linux Server from Linux/Windows using paramiko of python
Paramiko module(Used to work with remote servers):
=> Paramiko module will create a SSH client andby using this it will connect
   to remote server and execute commands.
=> We can also transfer files from the remote machine to the local or vice versa using paramiko
=> Two ways to connect with remote server:
   => Using username and password
   => Using username and cryptographic key
=> We connect to Linux/Windows <-> Linux/Windows

Local server        Remote server
------------        -------------
Windows             Windows
Windows             Linux
Linux               Linux
Linux               Windows

pip install paramiko
===================================================================================================
'''
'''
Local server: Windows, Remote server: Linux
'''
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.56.15",username="osboxes",password="osboxes.org",port=22)
stdin, stdout, stderr=ssh.exec_command('free -m')
print("The output is: ")
print(stdout.read())
print("The error is: ")
print(stderr.read())
ssh.close()
'''
Local server: Linux, Remote server: Linux
=> Create ssh keys and exchange the keys with remote
ssh-keygen
ssh-copy-id osboxes@192.168.56.15
pwd: osboxes.org

'''
'''
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.56.15",username="osboxes",key_filename="/home/osboxes/.ssh/id_rsa",port=22)
stdin, stdout, stderr=ssh.exec_command('free -m')
print("The output is: ")
print(stdout.read())
print("The error is: ")
print(stderr.read())
ssh.close()
'''
