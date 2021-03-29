'''
==================================
if is called simple conditional statement.
Used to control the execution of set of lines or block of code or one line

if expression:
    statement1
    statement2
==================================
'''
'''
import os
t_w=os.get_terminal_size().columns
given_str=input("Enter your string: ")
user_cnf=input("Do you want to align your text: Say yes or no?")
if user_cnf="yes":
    print(given_str.center(t_w).title())
    print(given_str.ljust(t_w).title())
    print(given_str.rjust(t_w).title())
'''

'''
user_str=input("Enter your string: ")
user_cnf=input("Do you want to convert your text into lowercase: Say yes or no?")
if user_cnf="yes":
    print(user_str.lower())
'''

'''
list_of_names=["Sam","Peter","John","Raghu"]
your_name=input("Enter your name: ")
if your_name in list_of_names:
    print("Congratulations!!Your name exists in our list.")
'''
