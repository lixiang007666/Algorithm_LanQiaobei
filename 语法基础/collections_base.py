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


d=deque()
d.append(1)
print(d)
d.appendleft(2)
print(d)
d.pop()
print(d)
d.popleft()
print(d)
nums=[1,1,2,3,4,5,5,6,6]
datas = Counter(nums)
a=[1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3]
print(Counter(a))
print(datas)
print(datas[1])
print(datas[4])
for each in datas.keys():
    if datas[each] == 1:
        print(each)


