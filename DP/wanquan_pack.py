import math
import cmath
import string
import sys
import bisect
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from itertools import permutations,combinations
from collections import deque,Counter
from functools import cmp_to_key,reduce

if __name__=="__main__":
    t,m=list(map(int,input().strip().split()))
    w=[]
    val=[]
    w.append(0)
    val.append(0)
    for i in range(m):
        x,y=list(map(int,input().strip().split()))
        w.append(x)
        val.append(y)
    dp=[0 for _ in range(1000005)]
    for i in range(1,m+1):
        j=t
        while j>=0:
            for k in range(0,j//w[i]+1):
                if j>=k*w[i]:#!!!!!   这里要✖️k
                    dp[j]=max(dp[j],dp[j-k*w[i]]+k*val[i])
            j-=1
    print(dp[t])



if __name__=="__main__":
    t,m=list(map(int,input().strip().split()))
    w=[]
    val=[]
    w.append(0)
    val.append(0)
    for i in range(m):
        x,y=list(map(int,input().strip().split()))
        w.append(x)
        val.append(y)
    dp=[0 for _ in range(10000001)]
    for i in range(1,m+1):
        j=0
        while j<=t:
            if j>=w[i]:
                dp[j]=max(dp[j],dp[j-w[i]]+val[i])
            j+=1
    print(dp[t])

