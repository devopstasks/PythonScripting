'''
=====================
Working with csv files using python
=> CSV - Comma Separated Value
=> It is a simple file format used to store tabular data, such as a
   spreadsheet/excel or database.
=> CSV is convenient way to export data to spreadsheets and databases as well as
   import or use it in other programs.
=====================
'''
'''
import csv
req_file="D:\\SAMPLE-PROJECTS\\PythonScripting\\info.csv"
fo=open(req_file,'r')
data=csv.reader(fo)
for each in data:
    print(each)
fo.close()
'''
import csv
req_file="D:\\SAMPLE-PROJECTS\\PythonScripting\\info.csv"
fo=open(req_file,'r')
#data=csv.reader(fo,delimiter=',')
data=csv.reader(fo,delimiter='|')
for each in data:
    print(each)
fo.close()
