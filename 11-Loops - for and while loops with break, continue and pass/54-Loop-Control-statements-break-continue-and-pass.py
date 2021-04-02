'''
=============
Loop control statements
=> break
   continue
   pass
=============
'''
'''
for each in [2,3,5,6]:
    if each==5:
        break
    print(each)
print("after loop")
'''
'''
paths=['/usr/bin','/usr/bin/httpd','/home/users/xyz/weblogic/config.xml']
for each_path in paths:
    print("now working on: ",each_path)
    if 'httpd' in each_path:
        print(each_path)
        break
print("outside of for loop")
'''
'''
for each in range(1,11):
    if each==7:
        continue
    print(each)
'''
'''
#while True:
while True:
    pass
#for each in range(5):
for each in range(5):
    pass
'''
