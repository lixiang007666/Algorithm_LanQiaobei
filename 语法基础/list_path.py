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

ls=[1,3,2]
print(len(ls))
#append() pop() remove() extend() clear() insert(a,b) reverse() count() index() del
print(ls[:])
print(ls[3::-1])
ls2=[5,54,5,874,8514,1,236,7,8,2]
print(ls2[:4])
for i in range(1,10):
    print(i,end=" ")
print()
for i in range(1,10,2):
    print(i,end=" ")
print()
for i in range(10,0,-2):
    print(i,end=" ")
print()
for i in range(10,-1,-1):#!!!!!!!!!!!!!
    print(i,end=" ")
print()
print(ls)
del ls[0]
print(ls)