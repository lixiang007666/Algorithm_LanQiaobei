import math
import cmath
import sys
import string
import bisect
import heapq
import copy
from queue import Queue,PriorityQueue,LifoQueue
from collections import Counter,deque
from itertools import permutations,combinations
from functools import cmp_to_key,reduce
a = [[1,2], [2,4], [1,3]]
b=[]
for i in range(3):
    b.append(list(map(int,input().strip().split())))

a.sort(key=lambda x: (x[0], -x[1]))
print(a)
b.sort(key=lambda x: (x[0], -x[1]))
print(b)