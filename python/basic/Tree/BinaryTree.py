#coding:utf-8
#author:Mike
#date:2019-10-08
#  二叉树的定义及遍历   

class BinaryTree(object):
	def __init__(self, obj):
		self.key = obj  
		self.leftchild = None 
		self.rightchild = None 
	def insertLeft(self,newNode):
		if self.leftchild == None:
			self.leftchild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.leftchild = self.child  
			self.child  = t  
	def insertRight(self,newNode):
		if self.rightchild == None:
			self.rightchild = BinaryTree(newNode)
		else:
			t = BinaryTree(newNode)
			t.rightchild = self.rightchild
			self.rightchild = t 
	def getRightchild(self):
		return self.rightchild
	def getLeftchild(self):
		return self.leftchild

	def setRoot(self,value):
		self.key = value
	def getRoot(self):
		return self.key  

	def preorder(self):
		print(self.key)
		if self.leftchild:
			self.leftchild.preorder()
		if self.rightchild:
			self.rightchild.preorder()


	def midOrder(self):
		if self.leftchild:
			self.leftchild.midOrder()
		print(self.key)
		if self.rightchild:
			self.rightchild.midOrder()


	def postOrder(self):
		if self.leftchild:
			self.leftchild.postOrder()
		if self.rightchild:
			self.rightchild.postOrder()
		print(self.key)





r = BinaryTree('a')
r.insertRight('c')
r.insertLeft('b')

print(r.getRoot())
print(r.getLeftchild())
print(r.getRightchild())

print(r.getLeftchild().getRoot())
print(r.getRightchild().getRoot())

r.preorder()
print('\n')
r.midOrder()
print('\n')
r.postOrder()

