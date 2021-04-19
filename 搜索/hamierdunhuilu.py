import math
import cmath
import sys
import string
import bisect
import heapq
from itertools import permutations, combinations
from queue import Queue, LifoQueue, PriorityQueue
from collections import Counter, deque
from functools import cmp_to_key

flag = 0
step = 0
map1 = [[0 for i in range(25)] for j in range(25)]
vis = [0 for i in range(25)]


def dfs(u, n):
    global flag
    global step
    if u == 0 and step == n + 1:
        flag = 1
    if flag == 1:
        return
    for i in range(n + 1):
        if not vis[i] and map1[u][i] == 1:
            vis[i] = 1
            step += 1
            dfs(i, n)
            step -= 1
            vis[i] = 0
    return


if __name__ == "__main__":
    n = int(input())
    for i in range(1, n + 1):
        list1 = list(map(int, input().strip().split()))
        for j in range(0, len(list1)):
            map1[i][list1[j]] = 1
            map1[list1[j]][i] = 1
    for i in range(6):
        for j in range(6):
            print(map1[i][j], end=" ")
        print()
    dfs(0, n)
    if flag == 1:
        print("yes")
    else:
        print("no")

