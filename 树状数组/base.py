import math
import sys
import string
import cmath
import bisect
import copy
import heapq
from collections import deque, Counter
from itertools import permutations, combinations
from queue import Queue, LifoQueue, PriorityQueue
from functools import cmp_to_key, reduce

N = 100000
arr = [0] * N#树桩数组

#单点修改
def add(i, j):
    while i < N:
        arr[i] += j
        i += i & -i


def sub(i, j):
    add(i, -j)


def sum(i):
    ans = 0
    while i > 0:
        ans += arr[i]
        i -= i & -i
    return ans

#区间查询 借助sum函数 这里不是普通的前缀和 而是借助于树状数组改进的前缀和
def query(i, j):
    return sum(j) - sum(i - 1)


if __name__ == "__main__":
    n, q = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    for i in range(1, len(a) + 1):
        add(i, a[i - 1])
    # print(arr)
    for i in range(q):
        id, x, y = list(map(int, input().strip().split()))
        if id == 1:
            add(x, y)
        else:
            print(query(x, y))

