#coding:utf-8  


class Stack(object):
	"""docstring for Stack"""
	def __init__(self,):
		self.items = []
	def isEmpty(self):
		return self.items==[]
	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def size(self):
		return len(self.items)






def main():

	s = Stack()
	for i in range(8):
	   s.push(i)

	print s.isEmpty()
	print s.size()
	a = []
	for i in range(s.size()):		
		a.append(s.pop())

	print a   


if __name__ == '__main__':
	main()

