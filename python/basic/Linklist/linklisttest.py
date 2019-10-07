#coding:utf-8
import Linklist



def main():
	
	link = Linklist.Linklist()

	for i in range(10):
		link.append(i)

	# print(link)
	print(link.getIndex(4))
	link.update(1,22)
	link.delete(0)
	print(link.getItem(0))
	print(link.getItem(4))


main()
