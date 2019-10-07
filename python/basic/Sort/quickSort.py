#coding:utf-8
#author:Mike
#date:2019-10-07
##原理参考 https://blog.csdn.net/qq_20011607/article/details/82357239



def quickSort(alist):
	quickSortHelper(alist,0,len(alist)-1)


def quickSortHelper(alist,first,last):
	if first<last:

		splitpoint = partion(alist,first,last)

		quickSortHelper(alist,first,splitpoint)
		quickSortHelper(alist,splitpoint+1,last)

def partion(alist,first,last):
	value = alist[first]

	left = first+1
	right = last

	finish = False  

	while not finish:

		while left<=right and alist[first+1]<=value:
			first = first+1  

		while alist[right]>=value and right>left:
			right = right-1  

		if right < left:
			finish = True
		else:
			temp = alist[first]
			alist[left] = alist[right]
			alist[right] = temp  

	temp = alist[first]
	alist[first] = alist[right]
	alist[right] = temp

	return right






alist2 = [6,5,3,4,2,1,7]
quickSort(alist2)
print alist2