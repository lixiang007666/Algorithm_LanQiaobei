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


#S[i] = a[1] + a[2] + … a[i]
#a[l] + … + a[r] = S[r] - S[l - 1]
if __name__ == "__main__":
    n, m = map(int, input().strip().split())
    a = []
    a.append(0)
    a.extend(map(int, input().strip().split()))
    s = [0 for i in range(100010)]
    # a=[0 for i in range(100010)]
    # for i in range(1,n+1):
    # print(a)
    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]
    while m:
        l, r = map(int, input().strip().split())
        print(s[r] - s[l - 1])
        m -= 1





