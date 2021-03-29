'''
=======================================
Practice with platform and os modules
=> Write a single python script to clear terminal of any operating system
   (or)
   Write a platform independent script to clear terminal
=======================================
'''
import os
import platform
if platform.system() == "Windows":
    os.system("cls")
else:
    os.system("clear")
