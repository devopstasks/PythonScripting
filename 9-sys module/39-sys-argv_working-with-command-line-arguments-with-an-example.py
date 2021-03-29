'''
====================================================
sys.argv of sys modules
=> sys.argv returns a list of command line arguments passed to a Python script.
====================================================
'''
'''
import sys
print(sys.argv)
'''
'''
user_str=input("Enter your string: ")
user_action=input("Enter your action on your string(valid actions are: lower/upper/title): ")
if user_action=="lower":
    print(user_str.lower())
elif user_action=="upper":
    print(user_str.upper())
elif user_action=="title":
    print(user_str.title())
else:
    print("Your option is invalid.Please select valid option from this list: lower/upper/title ")
'''
'''
import sys
user_str=sys.argv[1]
user_action=sys.argv[2]
if user_action=="lower":
    print(user_str.lower())
elif user_action=="upper":
    print(user_str.upper())
elif user_action=="title":
    print(user_str.title())
else:
    print("Your option is invalid.Please select valid option from this list: lower/upper/title ")
'''

import sys
if len(sys.argv) != 3:
    print("Usage:")
    print(f"{sys.argv[0]} <your_req_string> <lower|upper|title>")
    sys.exit()
user_str=sys.argv[1]
user_action=sys.argv[2]
if user_action=="lower":
    print(user_str.lower())
elif user_action=="upper":
    print(user_str.upper())
elif user_action=="title":
    print(user_str.title())
else:
    print("Your option is invalid.Please select valid option from this list: lower/upper/title ")
