import math
import cmath
import sys
import string
import bisect
import heapq
import copy
from itertools import permutations, combinations
from queue import Queue, LifoQueue, PriorityQueue
from collections import Counter, deque
from functools import cmp_to_key, reduce

# 从任意一个顶点开始，每次选择与当前顶点最近的一个顶点，并将两点之间的边加入到树中
# 被选中的点构成一个集合，剩下的点是候选集
# 每次从已选择的点的集合中，查找花费最小的点，加入进来
# 同时在候选集中删去，
# 重复3和4，知道候选集中没有元素。

def cmp(key1, key2):
    return (key1, key2) if key1 < key2 else (key2, key1)


def prim(graph, init_node):
    visited = set()
    visited.add(init_node)
    candidate = set(graph.keys())
    candidate.remove(init_node)  ## add all nodes into candidate set, except the start node
    tree = []
    sum=0
    while len(candidate) > 0:
        edge_dict = dict()
        for node in visited:  ## find all visited nodes
            for connected_node, weight in graph[node].items():  # find those were connected
                if connected_node in candidate:
                    edge_dict[cmp(connected_node, node)] = weight
        edge, cost = sorted(edge_dict.items(), key=lambda kv: kv[1])[0]  ## find the minimum cost edge
        sum+=cost
        tree.append(edge)
        visited.add(edge[0])  # cause you dont know which node will be put in the first place
        visited.add(edge[1])
        candidate.discard(edge[0])  # same reason. discard wont raise an exception.
        candidate.discard(edge[1])
#使用discard和remove都可以删除set当中的元素，区别就是remove的元素在set当中没有的话会报错，而discard不会。
    return tree,sum


if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    graph_dict = {}
    for i in range(1, n + 1):
        graph_dict[i] = {}
    for i in range(m):
        x, y, d = list(map(int, input().strip().split()))
        graph_dict[x][y] = d
    print(graph_dict)
    min1=math.inf
    pat ,sum= prim(graph_dict,1)
    if len(pat) != (n - 1):
        print("orz")
    print(sum)


