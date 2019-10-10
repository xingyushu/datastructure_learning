#coding:utf-8

from bfs import Graph
from Queue.queue import Queue
# 有向无环图
def sortedTopology(graph):
    inDict = {}                     # 存储节点：节点入度
    zeroInQueue = Queue()           # 存储入度为零的节点
    for node in graph.nodes:        # 遍历图所有的节点
        inDict[node] = node.come    # 将节点与节点入度存入字典中
        if node.come == 0:          # 若存在节点入度为零则将节点放入队列中
            zeroInQueue.enqueue(node)
    result = []
    while not zeroInQueue.isEmpty():
        cur = zeroInQueue.dequeue()
        result.append(cur)
        for next in cur.nexts:                  # 若当前节点邻接节点存在
            inDict[next] = inDict[next] - 1     # 在字典中将邻接节点入度减一再放回
            if inDict[next] == 0:
                zeroInQueue.put(next)
    return result