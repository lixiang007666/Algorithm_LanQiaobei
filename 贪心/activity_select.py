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


activitys=[(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
#保证活动按照结束时间排好序
activitys.sort(key=lambda x:x[1])

def fun(a):
    res=[a[0]]
    for i in range(1,len(a)):
        if a[i][0]>=res[-1][1]:
            res.append(a[i])
    return res

print(fun(activitys))
