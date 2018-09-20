# _*_coding:utf-8_*_
import heapq
import math

gragh = {
    'A':{'B':5, 'C':1},
    'B':{'A':5, 'C':2, 'D':1},
    'C':{'A':1, 'B':2, 'D':4, 'E':8},
    'D':{'B':1, 'C':4, 'E':3, 'F':6},
    'E':{'C':8, 'D':3},
    'F':{'D':6}
}

def initDistance(gragh, node):
    distance = {node: 0}
    for vertex in gragh:
        if vertex != node:
            distance[vertex] = math.inf
    return distance

def dijkstra(gragh, node):
    pqueue = []
    heapq.heappush(pqueue, (0, node))
    seen = set()
    parent = {node : None}
    distance = initDistance(gragh, node)
    while len(pqueue)>0:
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        nodes = gragh[vertex].keys()
        seen.add(vertex)
        for node in nodes:
            if node not in seen:
                if dist + gragh[vertex][node] < distance[node]:
                    heapq.heappush(pqueue, (dist + gragh[vertex][node], node))
                    parent[node] = vertex
                    distance[node] = dist + gragh[vertex][node]
    return parent, distance

if __name__ == '__main__':
    parent, distance = dijkstra(gragh, 'A')
    print(parent)
    print(distance)
