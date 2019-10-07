#coding:utf-8


class Person(object):
	"""docstring for Person"""
	def __init__(self, name,lang,address):
		# super(Person, self).__init__()
		self.name = name
		self.lang = lang
		self.address = address

		print('self',self)
		print('type of self',type(self))
	def syahi(self):
		print("hello I am",self.name)




p = Person('Mike','French','Paris')
p.syahi()