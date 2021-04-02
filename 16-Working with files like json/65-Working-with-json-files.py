'''
=============================
Working with json files using python
JSON
=> JSON(JavaScript Object Notation) is a popular data format used for representing structured data.
=> It's common to transmit and receive data between a server and web application in JSON format
Python          JSON equivalent
------          ---------------
dict            object
list,tuple      array
str             string
int,float       number
True            true
False           false
None            null
=============================
'''
'''
import json
req_file="D:\\SAMPLE-PROJECTS\\PythonScripting\\Sample.json"
fo=open(req_file,'r')
#print(fo.read())
#print(json.load(fo))
print(json.load(fo).get("glossary"))
fo.close()
'''
import json
req_file="D:\\SAMPLE-PROJECTS\\PythonScripting\\MyInfo.json"
my_dict={'Name':'Ram','Skills':['Python',"Shell","YAML","JSON","AWS"]}
fo=open(req_file,'w')
#json.dump(my_dict,fo)
json.dump(my_dict,fo,indent=4)

fo.close()
