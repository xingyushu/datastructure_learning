#coding:utf-8


class Queue(object):
	"""docstring for Queue"""
	def __init__(self):
		self.items  = []
	def enqueue(self,item):
		self.items.insert(0,item)
	def dequeue(self):
		return self.items.pop()
	def isEmpty(self):
		return self.items==[]
	def size(self):
		return len(self.items)



q = Queue()
for i  in range(5):
	q.enqueue(i)


for i in range(q.size()):
      print(q.dequeue())


def hotgame(names,num):
	a  = []
 	q1 = Queue()
 	for name in names:
 		q1.enqueue(name)

 	while q1.size()>1:
 		for i in range(num):
 			q1.enqueue(q1.dequeue())

 		# a.append(q1.dequeue())
 		q1.dequeue()

 	return q1.dequeue()


print(hotgame(["mike","bob","alice","mark","park","Bill"],7))