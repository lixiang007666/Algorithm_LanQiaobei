# B[i]=a[i]-a[i-1]
# 给区间[l, r]中的每个数a[]加上c：B[l] += c, B[r + 1] -= c
#求一个数组的差分，再求前缀和，他仍然是愿数组!!!!!!!

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

a = []
b = [0 for i in range(100010)]


def insert(l, r, c):
    b[l] += c
    b[r + 1] -= c


if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    a.append(0)
    a.extend(map(int, input().strip().split()))
    for i in range(1, n + 1):
        b[i] = a[i] - a[i - 1]
    while m:
        l, r, c = map(int, input().strip().split())
        insert(l, r, c)
        m -= 1
    ans = 0
    for i in range(1, n + 1):
        ans += b[i]
        print(ans, end=" ")





