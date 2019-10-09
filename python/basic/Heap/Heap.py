#coding:utf-8
#author:Mike
#date:2019-10-09
#  堆的定义及操作  
# 原理参考： https://www.cnblogs.com/sxkgeek/p/9662491.html

class Heap(object):
	"""docstring for Heap"""
	def __init__(self):
		self.heapList = [0]
		self.currentSize  = 0 

	def percUp(self,i):
		while i//2 >0:
			if self.heapList[i] <self.heapList[i//2]:
				tmp =  self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]
				self.heapList[i] = tmp  
			i = i//2   
	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize+1
		self.percUp(self.currentSize)

	def percDown(self,i):
		while(i*2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp  =  self.heapList[i]
				self.heapList[i] = self.heapList[mc]
				self.heapList[mc] = tmp  
			i = mc  


	def minChild(self,i):
		if i*2+1 > self.currentSize:
			return i*2  
		else:
			if self.heapList[2*i] < self.heapList[i*2+1]:
				return 2*i  
			else:
				return i*2+1   

	def delMin(self):
		retval  = self.heapList[1]
		self.heapList[1]= self.heapList[self.currentSize]
		self.currentSize = self.currentSize -1   
		self.heapList.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,alist):
		i = len(alist)//2  
		self.currentSize = len(alist)
		self.heapList = [0]+ alist[:]
		while (i>0):
			self.percDown(i)
			i = i -1   


heap =  Heap()
heap.buildHeap([9,5,7,2,3])
print(heap.delMin())







		
    