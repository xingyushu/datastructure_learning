#coding:utf-8
#author:Mike
#date:2019-10-10



class Vertex(object):
	"""docstring for Vertex"""
	def __init__(self, key):
		self.id = key
		self.connectTo = {}

	def addNeighbor(self,neighbor,weight=0):
		self.connectTo[neighbor] = weight

	def getConnections(self):
		return self.connectTo.keys()

	def getId(self):
		return self.id  

	def getWeight(self):
		return self.connectTo[neighbor]


class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.vertList = {}
		self.numNode = 0 

	def addVertex(self,key):
		self.numNode = self.numNode +1 
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None  

	def addEdge(self,f,t,cost=0):
		if f not in self.vertList:
			nv = self.vertList.addVertex(f)
		if t not in self.vertList:
			nv = self.vertList.addVertex(t)

		self.vertList[f].addNeighbor(self.vertList[t],cost)

	# def showEdge(self):
	# 	return  self.vertList.getConnections()

	def  getVertices(self):
		return self.vertList.keys()

	def __contain__(self,n):
		return n in self.vertList

	def __iter(self):
		return iter(self.vertList.values())


g = Graph()  
for i in range(6):
	g.addVertex(i)

print(g.vertList)

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)
print(g.getVertices())
# print(g.showEdge())
