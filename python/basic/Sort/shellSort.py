#coding:utf-8
#author:Mike
#date:2019-10-07
##原理参考 https://www.cnblogs.com/chengxiao/p/6104371.html


def shellSort(alist):
	sub = len(alist)//2
	while sub>0:
		for start in range(sub):
			gapInsertSort(alist,start,sub)
		print("after increment of size:",sub)


		sub = sub//2


def gapInsertSort(alist,start,gap):
	for i in range(start+gap,len(alist),gap):
		position = i  
		currentvalue = alist[i]


		while position>0 and alist[position-gap]>currentvalue:
			alist[position] = alist[position-gap]
			position = position-gap

		alist[position] = currentvalue



alist2 = [6,5,3,4,2,1,7]
shellSort(alist2)
print alist2
