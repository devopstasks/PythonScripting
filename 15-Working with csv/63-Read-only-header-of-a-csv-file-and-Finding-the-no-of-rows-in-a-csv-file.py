'''
===========================
Working with csv files using python
=> How to get header and no of rows in a csv file
===========================
'''
import csv
req_file="D:\\SAMPLE-PROJECTS\\PythonScripting\\info.csv"
fo=open(req_file,'r')
content=csv.reader(fo,delimiter="|")
#print(list(content)[0])
#print(f"The header is: \n{list(content)[0]}")
#print(next(content))
header=next(content)
print(f"The header is: ",header)
#print(f"The no of rows are: {len(list(content))}")
print("The contents are:")
for each in content:
    print(each)
fo.close()
