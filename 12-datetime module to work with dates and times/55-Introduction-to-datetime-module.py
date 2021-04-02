'''
===============================
datetime module
=> It is a built-in module and used to work with dates and times
   date
   time
   datetime
=> import datetime
   dir(datetime)
   dir(datetime.datetime)
===============================
'''
'''
import datetime
import pytz
req_timez=pytz.timezone('Asia/Kolkata')
print(datetime.datetime.now(req_timez)) #It prints the datetime in the provided timezone
strftime("") #Here we provide the datetime format
#Note: Use strftime.org to know the datetime format in python
'''
import datetime
import pytz
print(datetime.datetime.now())
print(datetime.datetime.today())
print(datetime.datetime.now().year)
print(datetime.datetime.now().month)
print(datetime.datetime.now().day)
print(datetime.datetime.now().hour)
print(datetime.datetime.now().minute)
print(datetime.datetime.now().second)
req_timez=pytz.timezone('Asia/Kolkata')
print(datetime.datetime.now(req_timez))
print("-----------")

# Use strftime.org to get the datetime format and use as below
print(datetime.datetime.now().strftime("%a"))
print(datetime.datetime.now().strftime("%c"))
print(datetime.datetime.now().strftime("%Y/%m/%d"))
print("-----------")
print(datetime.datetime.fromtimestamp(15555555))

print("=====")
from datetime import datetime
print(datetime.now())
