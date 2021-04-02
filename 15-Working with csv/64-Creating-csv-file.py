'''
===========================
Working with csv files using python
=> Creating csv file
===========================
'''
'''
import csv
req_file="D:\\SAMPLE-PROJECTS\\PythonScripting\\newinfo.csv"
fo=open(req_file,'r')
csv_reader=csv.reader(fo,delimiter="|")
for each_row in csv_reader:
    print(each_row)
fo.close()
'''
'''
import csv
req_file="D:\\SAMPLE-PROJECTS\\PythonScripting\\demo.csv"
#fo=open(req_file,'w') #This enters a new empty line after each line
fo=open(req_file,'w',newline="") #This prevents enters a new empty line after each line
csv_writer=csv.writer(fo,delimiter=",")
csv_writer.writerow(['S_No','Name','Age'])
csv_writer.writerow(['1','John','20'])
csv_writer.writerow(['2','Peter','25'])
fo.close()
'''
import csv
req_file="D:\\SAMPLE-PROJECTS\\PythonScripting\\demo.csv"
my_data=[['S_No','Name','Age'],['1','John','20'],['2','Peter','25'],['3','Cleve','28']]
fo=open(req_file,'w',newline="")
csv_writer=csv.writer(fo,delimiter=",")
#csv_writer.writerow(['S_No','Name','Age'])
#csv_writer.writerow(['1','John','20'])
#csv_writer.writerow(['2','Peter','25'])
csv_writer.writerows(my_data)
fo.close()
