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

##数字拼接问题 贪心

li=[32,94,128,1286,6,71]

def fun(x,y):
    if x+y>y+x:
        return -1
    elif x+y<y+x:
        return 1
    else:
        return 0

def number_join(li):
    li=list(map(str,li))
    print(li)
    li.sort(key=cmp_to_key(fun))
    return "".join(li)

print(number_join(li))


