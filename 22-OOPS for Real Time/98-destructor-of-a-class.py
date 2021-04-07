'''
==========================================
Concept: Destructor of a class
Constructor:
=> A Constructor is a special method that is called by default whenever
   you create an object from a class.

Destructor:
=> Destructors are called when an object gets destroyed.
=> In Python, destructors are not needed as much needed in C++ because
   python has a garbage collector that handles memory management automatically.
==========================================
'''
class Person(object):
	def __init__(self,name,age):
		print("an object has been created")
		self.name=name
		self.age=age
		return None
	def __del__(self):
		print("object has been deleted")
		return None

per1=Person('Jhon',26)
