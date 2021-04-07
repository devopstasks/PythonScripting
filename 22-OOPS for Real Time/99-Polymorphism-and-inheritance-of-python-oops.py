'''
======================================
Concept: Inheritance and Polymorphism
Polymorphism:
=> Polymorphism allows us to define same methods in different classes.
=> This process is also called as method overloading.
Inheritance:
=> Inheritance is a mechanism that allows us to create a new class - known as
   child class - that is based upon an existing class - the parent class.
=> Advantage with Inheritance:
   This saves you from duplicating a lot of code.
======================================
'''
'''
======================
Polymorphism:
======================
class Tomcat(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None
	def display(self):
		print("This is from tocmat class")
		print(self.home)
		print(self.version)
		return None
class Apache(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None
	def display(self):
		print("This is from apache class")
		print(self.home)
		print(self.version)
		return None

tom_ob=Tomcat('/home/tomcat9','7.6')
apa_ob=Apache("/etc/httpd",'2.4')

tom_ob.display()
apa_ob.display()
'''


'''
======================
Inheritance:
======================
'''
class Tomcat(object):
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None
	def display(self):
		print(self.home)
		print(self.version)
		return None
class Apache(Tomcat): # Here "Tomcat" is parent class and "Apache" is the child class
	def __init__(self,home,ver):
		self.home=home
		self.version=ver
		return None
tom_ob=Tomcat('/home/tomcat9','7.6')
apa_ob=Apache("/etc/httpd",'2.4')


tom_ob.display()
apa_ob.display()
