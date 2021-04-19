import math
import cmath
import sys
import string
import heapq
import bisect
from queue import Queue,PriorityQueue,LifoQueue
from collections import Counter,deque
from itertools import permutations,combinations
from functools import cmp_to_key

#无向图的遍历

graph={
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D','E'],
    'D':['B','C','E','F'],
    'E':['C','D'],
    'F':['D']
}

def DFS(graph,a):
    queue=[]
    queue.append(a)
    seen=set()
    seen.add(a)
    while len(queue)>0:
        vetex=queue.pop()
        nodes=graph[vetex]
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vetex)

def BFS(graph,a):
    queue=[]
    queue.append(a)
    seen=set()
    seen.add(a)
    while len(queue)>0:
        vetex=queue.pop(0)
        nodes=graph[vetex]#!!!!!!
        for w in nodes:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vetex)

if __name__=="__main__":
    BFS(graph,"A")
    DFS(graph,"A")