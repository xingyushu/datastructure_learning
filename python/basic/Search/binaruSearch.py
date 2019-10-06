#coding:utf-8


def binarySearch(alist,item):
	# pos =  0  
	first = 0  
	last = len(alist)-1
	found = False 

	while first<last and not found:
		mid = (first+last)/2
		if alist[mid] == item:
			found = True  
		elif alist[mid] < item:
			first = mid+1
		else:
			last = mid-1
	return found    



alist = [1,2,5,6,7,8,3]
print binarySearch(alist,4)
print binarySearch(alist,6)