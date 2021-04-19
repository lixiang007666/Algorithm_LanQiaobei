import math
import cmath
import sys
import string
import bisect
import heapq
from itertools import permutations,combinations
from queue import Queue,LifoQueue,PriorityQueue
from collections import Counter,deque
from functools import cmp_to_key,reduce

graph = {1: {5: 44, 1: 118}, 2: {5: 181, 4: 192, 2: 254}, 3: {2: 262}, 4: {2: 214, 3: 26, 4: 233}, 5: {1: 221, 4: 3}}

def initdis(graph,s):
    distance={s:0}
    for vertex in graph.keys():
        if vertex !=s:
            distance[vertex]=math.inf
    return distance

def fun(graph,s):
    pqueue=[]
    heapq.heappush(pqueue,(0,s))
    seen=set()
    parent={s:None}
    distance=initdis(graph,s)
    print(distance)
    while len(pqueue)>0:
        temp=heapq.heappop(pqueue)
        dist=temp[0]
        vertex=temp[1]
        seen.add(vertex)
        nodes=graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if (dist+graph[vertex][w])<distance[w]:
                    heapq.heappush(pqueue,(dist+graph[vertex][w],w))
                    parent[w]=vertex
                    distance[w]=dist+graph[vertex][w]
    return parent,distance

if __name__=="__main__":
    parent,distance=fun(graph,5)
    print(parent)
    print(distance)
# {'A': None, 'B': 'C', 'C': 'A', 'D': 'B', 'E': 'D', 'F': 'D'}
# {'A': 0, 'B': 3, 'C': 1, 'D': 4, 'E': 7, 'F': 10}
