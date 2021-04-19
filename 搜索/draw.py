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

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
b = []
a = []

#在数组外围加一圈 这样右下角就不会形成闭圈 就可以搜索到了
def dfs(p, q):
    if p < 0 or q < 0 or p > n+1 or q > n+1 or a[p][q] != 0:
        return
    a[p][q] = 1
    for i in range(1, 5):
        dfs(p + dx[i], q + dy[i])


if __name__ == "__main__":
    n = int(input())
    a = [[0 for i in range(n+2)] for j in range(n+2)]
    for i in range(n):
        temp = list(map(int, input().strip().split()))
        temp.insert(0,1)
        temp.append(1)
        b.append(temp)
    b.insert(0,[1 for _ in range(n+2)])
    b.append([1 for _ in range(n+2)])
    for i in range(1,n+1):
        for j in range(1,n+1):
            if b[i][j] == 0:
                a[i][j] = 0
            else:
                a[i][j] = 2
    for _ in b:
        print(_)
    print()
    for _ in a:
        print(_)
    print()
    dfs(0, 0)
    for _ in a:
        print(_)
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i][j] == 0:
                print(2, end=" ")
            else:
                print(b[i][j], end=" ")
        print()

