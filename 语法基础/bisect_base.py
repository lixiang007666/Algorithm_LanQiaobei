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

a = [1,4,6,8,12,15,20]
position = bisect.bisect(a,1)  #参数是数组+value
c=bisect.bisect(a,2)
b=bisect.bisect(a,22)
print(c)
print(position)
print(b)

a = [1,4,6,8,12,15,20]
bisect.insort(a,13)
bisect.insort(a,1)
print(a)

