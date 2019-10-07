#coding:utf-8
#author:Mike
#date:2019-10-07

def MergeSort(alist):
	if len(alist)>1:
		mid = len(alist)//2 
		left = alist[:mid]
		right = alist[mid:]

		MergeSort(left)
		MergeSort(right)


		i = 0 
		j = 0
		k = 0  

		while i<len(left) and j<len(right):
			if left[i] < right[j]:
				alist[k] = left[i]
				i = i+1  
			else:
				alist[k] = right[j]
				j = j+1 
			k = k+1  

		while i<len(left):
				alist[k] = left[i]
				i = i+1  
				k = k+1 

		while j<len(right):
				alist[k] = right[j]
				j = j+1  
				k = k+1 
	print("after MergeSort:",alist)




alist2 = [6,5,3,4,2,1,7]
MergeSort(alist2)
print alist2