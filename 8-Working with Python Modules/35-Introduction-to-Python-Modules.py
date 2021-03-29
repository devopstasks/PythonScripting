'''
======================================================
What is a module?
=> A module is a file containing python definitions and statements.That means module containing
python functions,classes and variables.

What is the use of module?
=> Reusability
ex: If script name is mymodule.py then module name is mymodule

Types of Python modules:
=> Default modules
=> Third-party modules
Note: Import either default or third party modules before using them.
======================================================
=======================================================
=> List all functions and variables of a module using the dir() function
=> Getting help of a particular module
=> from script: print(help(math))
   from python command line: help(math)

import math
dir(math)
help(math)

=> install a third-party module
pip install <module-name>
pip install xlrd
pip install xlwt
import xlrd
import xlwt
dir(xlrd)
help(xlrd)
dir(xlwt)
help(xlwt)
======================================================
=======================================================
Method-1
========
import math
print(math.pi)
print(math.pow(3,2))

Method-2
========
import math as m
print(m.pi)
print(m.pow(3,2))

Method-3
========
from math import *
print(pi)
print(pow(3,2))

Method-4
========
from math import pi,pow
print(pi)
print(pow(3,2))

=========
import platform
import math
import sys
import os
import subprocess

or

import platform,math,sys,os,subprocess

======================================================
'''
