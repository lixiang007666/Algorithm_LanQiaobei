import math
import cmath
import sys
import string
import heapq
import bisect
import copy
from queue import Queue,PriorityQueue,LifoQueue
from collections import Counter,deque
from itertools import permutations,combinations
from functools import cmp_to_key,reduce

def fun(arr,p,r,x):
    if p==r:
        if arr[p]==x:
            return 1
        else:
            return 0
    else:
        q=(p+r)//2
        return fun(arr,p,q,x)+fun(arr,q+1,r,x)

if __name__=="__main__":
    arr=[1,2,34,43,242,242,242,245]
    x=int(input())
    n=fun(arr,0,7,x)
    print(n)