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

if __name__=="__main__":
    a=[3,12,5,2,9,12]
    b=[8,10,9,6,3,1]
    s1={}
    s2={}
    for i in range(len(a)):
        if a[i]<b[i]:
            s1[i]=a[i]
        else:
            s2[i]=b[i]
    s1=sorted(s1.items(),key=lambda x:x[1])
    s2=sorted(s2.items(),key=lambda x:x[1],reverse=True)
    c=[]
    print("最优作业调度顺序为：")
    for i in s1:
        c.append(i[0])
    for i in s2:
        c.append(i[0])
    for _ in c:
        print(_+1,end=" ")
    sum=0

