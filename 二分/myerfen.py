import sys
import math
import cmath
import bisect
import string
import heapq
import copy
from itertools import combinations, permutations
from collections import Counter, deque
from queue import LifoQueue, Queue, PriorityQueue
from functools import cmp_to_key,reduce

def fun(a,x):
    left=0
    right=len(a)
    while left<right:
        mid = (left + right) // 2
        if x<a[mid]:
            right=right-1
        elif x>a[mid]:
            left=left+1
        else:
            return mid
    return False



if __name__ == "__main__":
    a = [5, 4, 645, 2, 78, 76, 68, 223, 98]
    a.sort()
    print(a)
    print(fun(a,5))
    print(fun(a,1))
    print(fun(a,800))