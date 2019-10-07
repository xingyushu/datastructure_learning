# coding:utf-8
class Node(object):
	"""docstring for ClassName"""
	def __init__(self,data):
		self.data = data
		self.next  = None
	def getData(self):
		return self.data 
	def __repr__(self):
		return str(self.data)

class Linklist(object):
	"""docstring for """
	def __init__(self):
		self.head = None
		self.length =0 

	def isEmpty(self):
		return (self.length == 0)


	def append(self,data):
		item = None
		if isinstance(data,Node):
			item = data
		else:
			item = Node(data)

		if not self.head:
			self.head = item
			self.length += 1

		else:
			node = self.head
			while  node.next:
				node = node.next
			node.next = item
			self.length += 1



	def delete(self,index):
		if self.isEmpty():
			print("this is a vacant chain")
			return 
		if index <0 or index >self.length:
			print("wrong index") 
			return

		if index == 0:
			self.head = self.head.next
			self.length -= 1
			return

		j = 0
		node = self.head
		prev = None

		while node.next and j <index:
			prev = node
			node = node.next
			j += 1

		if j == index:
			prev.next = node.next
			self.length -= 1


	def insert(self,index,data):
		if self.isEmpty():
			print("this is a vacant chain")
			return 
		if index <0 or index >self.length:
			print("wrong index") 
			return

		item = None
		if isinstance(data,Node):
			item = data
		else:
			item = Node(data)

		if index == 0 :
			item.next = self.head
			self.head = item
			self.length += 1
			return

		j = 0
		node = self.head
		prev = self.head

		while node.next and j <index:
			prev = node
			node = node.next
			j += 1

		if j == index:
			item.next = node
			prev.next = item
			self.length += 1


	def update(self,index,data):
		if self.isEmpty():
			print("this is a vacant chain")
			return 
		if index <0 or index >self.length:
			print("wrong index") 
			return

		j = 0 
		node = self.head
		while  j<index  and node.next:
			node = node.next
			j += 1

		if j == index:
			node.data = data  

	def len(self):
		return self.length




	def clear(self):
		self.head = None
		self.length = 0




	def __repr__(self):
		pass



	def getItem(self,index):
		if self.isEmpty():
			print("this is a vacant chain")
			return 
		if index <0 or index >self.length:
			print("wrong index") 
			return

		j = 0 
		node = self.head
		while  node.next and j <index:
			node = node.next
			j += 1  

		return node.data

	def getIndex(self,data):
		if self.isEmpty():
			print("this is a vacant chain")
			return 


		j = 0 
		node = self.head
		while  node :
			if node.data == data:
				return j
			node = node.next
			j += 1  

		if j == self.length:
			print("index not found")
			return

	def __getItem__(self,indx):
		if self.isEmpty():
			print("this is a vacant chain")
			return 
		if index <0 or index >self.length:
			print("wrong index") 
			return

		self.getItem(indx)



	def __setItem__(self,indx,data):
		if self.isEmpty():
			print("this is a vacant chain")
			return 
		if index <0 or index >self.length:
			print("wrong index") 
			return

		self.update(indx,data)

	# def __str__(self):
	# 	return ('<%s:%s>' % (self.__class__.__name__, self.name))
		

