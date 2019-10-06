#coding:utf-8

def orderSearch(alist,item):
	found = False 
	i = 0
	while i<len(alist) and not found:
		if alist[i] == item:
			found = True  
		else:
			i = i+1  
	return found



alist=[1,4,3,8,7]
print orderSearch(alist,3)
print orderSearch(alist,9)