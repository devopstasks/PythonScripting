'''
============================
getpass() prompts the usser for a password without echoing.The getpass module provides a secure
way to handle the passsword prompts where program interact with the users via the terminal.

getuser() function displays the login name of the user. This function checks the environment variables
LOGNAME, USER, LNAME and USERNAME, in order, and returns the value of the first non-empty string.
============================
'''
'''
import getpass
#db_pass=getpass.getpass()
db_pass=getpass.getpass(prompt="Enter your DB Password: ")
print(f"The entered password is {db_pass}")
'''
