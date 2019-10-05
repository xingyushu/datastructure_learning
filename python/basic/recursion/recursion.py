#coding:utf-8  

def listsum(list1):
	if len(list1) == 1:
		return list1[0]
	else:
		return list1[0] + list1[1:]

def Fabonaci(b):
	if b == 1 or b==2:
		return 1
	else:
		return Fabonaci(b-1)+Fabonaci(b-2)
