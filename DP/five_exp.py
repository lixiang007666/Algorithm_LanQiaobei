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


#物品不选也有价值哦！
if __name__=="__main__":
    n,x=list(map(int,input().strip().split()))
    lose=[]
    val=[]
    w=[]
    lose.append(0)
    val.append(0)
    w.append(0)
    dp=[0 for _ in  range(1005)]
    for i in range(1,n+1):
        t,y,z=list(map(int,input().strip().split()))
        t*=5
        y*=5
        lose.append(t)
        val.append(y)
        w.append(z)
    for i in range(1,n+1):
        j=x
        while j>=0:
            if j>=w[i]:
                dp[j]=max(dp[j]+lose[i],dp[j-w[i]]+val[i])
            else:
                dp[j] = dp[j] + lose[i]
            j-=1
    print(dp[x])
