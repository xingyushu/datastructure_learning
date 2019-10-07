#coding:utf-8
#author:Mike
#date:2019-10-05

def bubbleSort(alist):
	for num in range(len(alist)-1,0,-1):
		for i in range(num):
			if alist[i]>alist[i+1]:
				temp = alist[i] 
				alist[i] = alist[i+1]
				alist[i+1] = temp  



alist = [6,5,3,4,2,1,7]
bubbleSort(alist)
print alist


#修改后的冒泡排序

def shortBubbleSort(alist):
	exchange = True  
	num = len(alist)-1
	while num>0:
		exchange = False 
		for i in range(num):
			if alist[i]>alist[i+1]:
				exchange = True 
				temp = alist[i] 
				alist[i] = alist[i+1]
				alist[i+1] = temp  
		num = num-1

	

alist2 = [6,5,3,4,2,1,7]
shortBubbleSort(alist2)
print alist2