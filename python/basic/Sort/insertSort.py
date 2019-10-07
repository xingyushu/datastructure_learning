#coding:utf-8
#author:Mike
#date:2019-10-06
#原理参考 https://www.cnblogs.com/9dragon/p/10710735.html

def insertSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index   

		while position>0 and alist[position-1]>currentvalue:
			alist[position] = alist[position-1]
			position = position-1

		alist[position] = currentvalue



alist2 = [6,5,3,4,2,1,7]
insertSort(alist2)
print alist2



