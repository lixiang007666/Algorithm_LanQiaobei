import math
import cmath
import sys
import string
import bisect
import heapq
from queue import Queue, LifoQueue, PriorityQueue
from itertools import combinations, permutations
from collections import Counter, deque
from functools import cmp_to_key,reduce


#单源最短路
graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D": 1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6}
}


def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph.keys():
        if vertex != s:
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)
    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)
        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                if (dist + graph[vertex][w]) < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = (dist + graph[vertex][w])
    return parent, distance


if __name__ == "__main__":
    parent, distance = dijkstra(graph, "A")
    print(parent)
    print(distance)




