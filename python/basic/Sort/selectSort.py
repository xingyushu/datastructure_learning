#coding:utf-8
#author:Mike
#date:2019-10-05


def selectSort(alist):
	for  i in range(len(alist)-1,0,-1):
		max = 0 
		for location in range(1,i+1):
			if alist[location]>alist[max]:	
				max =  location

		temp = alist[i] 
		alist[i] = alist[max]
		alist[max] = temp  




alist2 = [6,5,3,4,2,1,7]
selectSort(alist2)
print alist2