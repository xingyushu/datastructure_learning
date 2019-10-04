#coding:utf-8 

class Dequeue(object):
	"""docstring for Dequeue"""
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def addFront(self,item):
		self.items.append(item)
	def addRear(self,item):
		self.items.insert(0,item)

	def removeFront(self):
		return self.items.pop()
	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)



def check(string):
	d = Dequeue()

	for i in string:
		d.addRear(i)

	check1 = True
	while d.size()>1 and check1:
		first = d.removeFront()
		last = d.removeRear()
		if first != last:
			check1 = False

	return check1


print(check("abcba"))
print(check("abcbad"))
