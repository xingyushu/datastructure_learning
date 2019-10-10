#coding:utf-8
#author:Mike
#date:2019-10-09

class Node(object):
	"""docstring for Node"""
	def __init__(self, value):
		self.value = value
		self.come = 0
		self.out = 0  
		self.nexts = []
		self.edges =  []  


class Edge(object):
	"""docstring for Edge"""
	def __init__(self,weight,f,t):
		self.weight = weight
		self.fro = f 
		self.to = t 


class Graph(object):
			"""docstring for Graph"""
	def __init__(self):
		self.nodes = {}
		self.edges = {}


# 生成图结构
# matrix = [
#   [1,2,3],        ==>   里面分别代表权重, from节点, to节点
#   [...]
# ]
from Graph import Graph
from Node import Node
from Edge import Edge


def createGraph(matrix):
    graph = Graph()
    for edge in matrix:
        weight = edge[0]
        fro = edge[1]
        to = edge[2]
        if fro not in graph.nodes:
            graph.nodes[fro] = Node(fro)
        if to not in graph.nodes:
            graph.nodes[to] = Node(to)
        fromNode = graph.nodes[fro]
        toNode = graph.nodes[to]
        newEdge = Edge(weight, fromNode, toNode)
        fromNode.nexts.append(toNode)
        fromNode.out += 1
        toNode.come += 1
        fromNode.edges.append(newEdge)
        graph.edges.append(newEdge)
    return graph



# 图的广度优先遍历
# 1.利用队列实现
# 2.从源节点开始依次按照宽度进队列，然后弹出
# 3.每弹出一个节点，就把该节点所有没有进过队列的邻接点放入队列
# 4.直到队列变空
from queue import Queue
def bfs(node):
    if node is None:
        return
    queue = Queue()
    nodeSet = set()
    queue.enqueue(node)
    nodeSet.add(node)
    while not queue.isEmpty():
        cur = queue.dequeue()               # 弹出元素
        print(cur.value)                # 打印元素值
        for next in cur.nexts:          # 遍历元素的邻接节点
            if next not in nodeSet:     # 若邻接节点没有入过队，加入队列并登记
                nodeSet.add(next)
                queue.put(next)
						
