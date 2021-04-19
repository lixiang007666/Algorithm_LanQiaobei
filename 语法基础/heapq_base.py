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


lyst = [-3, 22, 45, 34, 99, 102, -44]

top3 = heapq.nlargest(3, lyst)
low3 = heapq.nsmallest(3, lyst)
print(low3,top3)

pqueue=[]
heapq.heappush(pqueue,(1,"A"))
heapq.heappush(pqueue,(2,"B"))
heapq.heappush(pqueue,(4,"C"))
heapq.heappush(pqueue,(7,"D"))
heapq.heappush(pqueue,(5,"E"))

print(heapq.heappop(pqueue))
print(heapq.heappop(pqueue))
print(heapq.heappop(pqueue))
print(heapq.heappop(pqueue))
print(heapq.heappop(pqueue))
