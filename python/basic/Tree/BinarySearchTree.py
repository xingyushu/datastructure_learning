#coding:utf-8
#author:Mike
#date:2019-10-09

class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self,val):
		self.val = val 
		self.left = None 
		self.right = None 



class SearchTree(object):
	"""docstring for SearchTree"""
	def __init__(self):
		self.root = None 

	def insert(self,root,val):
		if root == None:
			root = TreeNode(val)
		elif val<root.val:
			root.left = self.insert(root.left,val)
		else:
			root.right = self.insert(root.right,val)
		return root 

	def query(self,root,val):
		if root == None:
			return False 
		if root.val == val:
			return True  
		elif val< root.val:
			return self.query(root.left,val)
		else:
			return self.query(root.right,val)

	def findMin(self,root):
		if root.left:
			return self.findMin(root.left)
		else:
			return root  

	def findMax(self,root):
		if root.right:
			return self.findMax(root.right)
		else:
			return root  

	def delNode(self,root,val):
		if root == None:
			return 
		if val<root.val:
			root.left= self.delNode(root.left,val)
		elif val>root.val:
			root.right = self.delNode(root.right,val)

		else:
			if root.left and root.right:
				temp = self.findMin(root.right)
				root.val = temp.val
				root.right = self.delNode(root.right,temp.val)   
			elif root.right == None and root.left == None:
				root = None 
			elif root.right == None:
				root = root.left 
			elif root.left == None:
				root = root.right
		return root  

	def printTree(self, root):
			# 打印二叉搜索树(中序打印，有序数列)
		if root == None:
			return 
		self.printTree(root.left)
		print(root.val)
		self.printTree(root.right)

if __name__ == '__main__':
	List = [17,5,35,2,11,29,38,9,16,8]
	root = None
	op = SearchTree()
	for val in List:
		root = op.insert(root,val)
	print('中序打印二叉搜索树：')
	op.printTree(root)
	print('')
	print('根节点的值为：', root.val)
	print('树中最大值为:', op.findMax(root).val)
	print('树中最小值为:', op.findMin(root).val)
	print('查询树中值为5的节点:', op.query(root, 5))
	print('查询树中值为100的节点:', op.query(root, 100))
	print('删除树中值为16的节点:')
	root = op.delNode(root, 16)
	op.printTree(root)
	print('')
	print('删除树中值为5的节点:')
	root = op.delNode(root, 5)
	op.printTree(root)
	print('')




		

		


