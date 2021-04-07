'''
================================================================================
Windows Subsystem for Linux(WSL)
=> Windows Subsystem for Linux(WSL) is an optional feature on Windows 10
=> We can run Ubuntu, Fedora and OpenSUSE on Windows using WSL feature, and
   more linux distributions coming soon.
=> This feature doesn't work on the 32-bit version of Windows-10, so ensure
   you are using 64-bit version of Windows-10.
=> Advantage: We can ascess Windows Files in Bash, and Bash files in Windows.
=> Installation:
   => Open Start -> Turn Windows Features on and off -> Check Windows Subsystem for Linux
=> Restart  Windows 10.
=> Goto Microsoft store and search "linux" and install any version of linux.
=> #sudo su -
   #cd mnt
   #ls
   c e
   #cd e/
   #ls
   #mkdir Windows_Linux
   #cd Windows_Linux
=> Open the "Atom" or any editor and create a file "E:/Windows_Linux/demo.sh"
   write the code in the file
   demo.sh
   -------------
   #!/bin/bash
   echo "This file is created on my windows but we can access on Ubuntu"

=> Now execute this file in Ubuntu terminal.
   #./demo.sh
=> This is very simple ways for developers to test their code on both windows and linux.
================================================================================
'''
