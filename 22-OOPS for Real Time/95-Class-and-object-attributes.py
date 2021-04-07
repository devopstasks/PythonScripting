'''
=====================================
Concept: Class and Object Attributes
Class:
=> Class is a template/blueprint to create an object.
=> Class is the combinaation of attributes and methods.
=> We can define attributes for class and objects.
======================================
'''
class emp:
	count=0
	def get_name_age_salary(self,name,age,salary):
		self.name=name
		self.age=age
		self.salary=salary
		self.increase_count_for_emp()
		#self.display_details()
		return None
	def increase_count_for_emp(self):
		emp.count=emp.count+1
		return None
	def display_details(self):
		print(f'The name is: {self.name}\nThe age is: {self.age}\nThe salary is: {self.salary}')
		return None

emp1=emp()
emp2=emp()

emp1.get_name_age_salary('John',34,45000)
#emp1.increase_count_for_emp()
emp2.get_name_age_salary('Cliton',25,54000)
#emp2.increase_count_for_emp()
#print(dir(emp1)) #This prints the object properties
print(emp.count) # This is to show the Class level variable
