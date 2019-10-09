#coding:utf-8
#author:Mike
#date:2019-10-09


class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self,val):
		self.key = key  
		self.payload = val
		self.leftchild = None  
		self.rightchild = None  
		self.parent = None  

	def  hasLeftchild(self):
		return self.leftchild

	def hasRightchild(self):
		return self.rightchild

	def hasParent(self):
		return self.parent

	def isLeftChild(self):
		return self.parent and self == self.parent.leftchild

	def  isRightChild(self):
		return self.parent and self == self.parent.rightchild


	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightchild or self.leftchild)

	def hasAnychild(self):
		return self.leftchild or self.rightchild

	def  hasbothchild(self):
		return  self.leftchild and self.rightchild

	def updateData(self,mkey,val,lc,rc):
		self.key = key  
		self.payload = val
		self.leftchild = lc  
		self.rightchild = rc  
		if self.hasLeftchild():
			self.leftchild.parent = self 
		if self.hasRightchild():
			self.rightchild.parent =self

class BinarySearchTree(object):
	"""docstring for BinarySearchTree"""
	def __init__(self):
		self.root = None 
		self.size =0  
	def length(self):
		return self.size  
	def __len__(self):
		return self.size  

	def __iter__(self):
		return self.root.__iter__()

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root = TreeNode(key,val)
		self.size = self.size +1  

	def _put(self,key,val,currentNode):
		if key<currentNode.key:
			if currentNode.hasLeftchild():
				self._put(key,val,currentNode)
			else:
				currentNode.leftchild = TreeNode(key,val,parent=currentNode)
		else:
			if currentNode.hasRightchild():
				self._put(key,val,currentNode.rightchild)
			else:
				currentNode.rightchild = TreeNode(key,val,parent=currentNode)

	def __setitem(self,k,v):
		self.put(k,v)

	def get(self,key):
		if self.root:
			res = self._get(key,self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	def _get(self,key,currentNode):
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif key < currentNode.key:
			return self._get(key,currentNode.leftChild)
		else:
			return self._get(key,currentNode.rightChild)

	def __getitem__(self,key):
		return self.get(key)

	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False


	def delete(self,key):
		if self.size > 1:
			nodeToRemove = self._get(key,self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size = self.size-1
			else:
				raise KeyError('Error, key not in tree')
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size = self.size - 1
		else:
			raise KeyError('Error, key not in tree')
	def __delitem__(self,key):
		self.delete(key)


	def findSuccessor(self):
		succ = None
		if self.hasRightChild():
			succ = self.rightChild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
				succ = self.parent
				else:
				self.parent.rightChild = None
				succ = self.parent.findSuccessor()
				self.parent.rightChild = self
		return succ

	def findMin(self):
		current = self
		while current.hasLeftChild():
			current = current.leftChild
		return current

	def remove(self,currentNode):
		if currentNode.isLeaf(): #leaf
			if currentNode == currentNode.parent.leftChild:
				currentNode.parent.leftChild = None
			else:
				currentNode.parent.rightChild = None
		elif currentNode.hasBothChildren(): #interior
			succ = currentNode.findSuccessor()
			succ.spliceOut()
			currentNode.key = succ.key
			currentNode.payload = succ.payload
		else: # this node has one child
			if currentNode.hasLeftChild():
				if currentNode.isLeftChild():
				currentNode.leftChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.leftChild
				elif currentNode.isRightChild():
					currentNode.leftChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.leftChild
				else:
				currentNode.replaceNodeData(currentNode.leftChild.key,
				currentNode.leftChild.payload,
				currentNode.leftChild.leftChild,
				currentNode.leftChild.rightChild)
			else:
				if currentNode.isLeftChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.rightChild
				elif currentNode.isRightChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.rightChild
				else:
					currentNode.replaceNodeData(currentNode.rightChild.key,
					currentNode.rightChild.payload,
					currentNode.rightChild.leftChild,
					currentNode.rightChild.rightChild)




