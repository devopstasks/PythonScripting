'''
===========================
Concept: Encapsulation
=> Using OOPS in python, we can restrict access to methods and variables.
=> This prevent data from direct modification which is called encapsulation.
=> Keep double underscore before a variable or method can make them encapsulated.
   ex: self.name=name   -> not encapsulated
       self.__age=age   -> encapsulated
       self.__display() -> encapsulated
===========================
'''
class Person(object):
	def assing_name_and_age(self,name,age):
		self.name=name
		self.__age=age
		self.__display()
		return None
	def __display(self):
		print(self.name,self.__age)
		return None

per1=Person()
per1.assing_name_and_age('John',32)

#per1.__display()
#print(per1.name)
#print(per1.__age)
