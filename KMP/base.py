import math
import cmath
import sys
import string
import heapq
import bisect
from queue import Queue,PriorityQueue,LifoQueue
from collections import Counter,deque
from itertools import permutations,combinations
from functools import cmp_to_key,reduce

def Gen_next(str):
    j=-1
    i=0
    next=[-1]
    while i<len(str)-1:
        if j==-1 or str[i]==str[j]:
            i+=1
            j+=1
            next.append(j)
        else:
            j=next[j]
    print(next)
    return next

def kmp(s1,s2):
    next=Gen_next(s2)
    i=0
    j=0
    while i<len(s1) and j<len(s2):
        if j==-1 or s1[i]==s2[j]:
            i+=1
            j+=1
        else:
            j=next[j]
    if j>=len(s2):
        return i-len(s2)
    else:
        return 0

if __name__=="__main__":
    s1 = "acabaabaabcacaabc"  #文本串
    s2 = "abaabcac"#模式串
    print(kmp(s1, s2))
    a="1"
    b="1"
    print(kmp(a,b))




