'''
=============================================================================
Transfer a file from local server to remote server and vice versa using
paramiko of python
=============================================================================
'''
import paramiko
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname="192.168.56.15",username="osboxes",password="osboxes.org",port=22)
sftp_client=ssh.open_sftp()
#upload file from windows to linux
sftp_client.put('C:\\temp\\paramiko_upload_file.txt','/home/osboxes/paramiko_downloaded_file.txt')

sftp_client.chdir('/home/osboxes')
print(sftp_client.getcwd())
#download file from linux to windows
sftp_client.get('/home/osboxes/paramiko_1.txt','C:\\temp\\paramiko_from_linux.txt')
sftp_client.close()
ssh.close()
