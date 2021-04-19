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

#求最小子串的循环次数；

def Gen_next(str):
    j=-1
    i=0
    next=[-1]
    while i<len(str):
        if j==-1 or str[i]==str[j]:
            i+=1
            j+=1
            next.append(j)
        else:
            j=next[j]
    return next[1:]

if __name__=="__main__":
    s=input()
    a=Gen_next(s)
    print(a)
    j=len(s)
    k=a[-1]
    if j%(j-k)==0 and k!=0:
        print(j//(j-k))
    else:
        print(1)
