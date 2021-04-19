import math
import cmath
import string
import sys
import bisect
import heapq
from queue import Queue, LifoQueue, PriorityQueue
from itertools import permutations, combinations
from collections import deque, Counter
from functools import cmp_to_key
#每次通过倍增加速状态转移、预处理或查询（很多时候能把时间复杂度降到O(logN)
#在变化规则相同的情况下加速状态转移（如：快速幂，LCA（倍增法））
# 倍增预处理++最短路
#
# 我们首先预处理出来从一号节点走2^k2
# k
#  步可以到达的所有结点，然后用\text{floyd}floyd跑一遍最短路即可。
#
# 关键部分在预处理，我们要注意枚举顺序，外层枚举kk，然后内层再n^3n
# 3
#  枚举转移。
#
# 先枚举kk是为了在转移当前状态时，保证他前面所有的2^{1...k-1}2
# 1...k−1
#  步已经全部处理完成了。
#
# 于是代码就很好写了。
g = [[math.inf for _ in range(55)] for _ in range(55)]
f = [[[0 for _ in range(34)] for _ in range(55)] for _ in range(55)]
n = 0


def pre():#倍增预处理
    for p in range(1, 33):
        for k in range(1, n + 1):
            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if f[i][k][p - 1] and f[k][j][p - 1]:
                        f[i][j][p] = 1
                        g[i][j] = 1
    for i in range(1,n+1):
        g[i][i]=0

def floyed():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j and j != k and i != k:
                    g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    print(g[1][n])


if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    for i in range(m):
        u, v = list(map(int, input().strip().split()))
        g[u][v] = 1
        f[u][v][0] = 1
    pre()
    floyed()


