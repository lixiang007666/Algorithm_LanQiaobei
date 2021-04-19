import copy
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
#求某一个字符串的相等的前后缀长度，并按照长度从小到大输出
#next[18]=9 next[9]=4 next[4]=2 next[2]=0结束

if __name__=="__main__":
    str=input()
    i=0
    j=-1
    next=[-1]
    while i<len(str):
        if j==-1 or str[i]==str[j]:
            i+=1
            j+=1
            next.append(j)
        else:
            j=next[j]
    print(len(str),end=" ")
    i=len(str)
    while next[i]!=0:
        print(next[i],end=" ")
        i=next[i]



