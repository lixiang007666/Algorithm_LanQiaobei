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
    #t表示重量 m表示物体个数
    w=[]
    val=[]
    w.append(0)
    val.append(0)
    for i in range(m):
        x,y=list(map(int,input().strip().split()))
        w.append(x)
        val.append(y)
    dp=[[0 for _ in range(1005)] for _ in range(105)]
    for i in range(1,m+1):
        j=t#j 从右往左
        while j>=0:
            if j>=w[i]:#！！！！！！
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-w[i]]+val[i])
            else:
                dp[i][j]=dp[i-1][j]
            j-=1
    print(dp[m][t])



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
    dp=[0 for _ in range(1005)]
    for i in range(1,m+1):
        j=t
        while j>=0:
            if j>=w[i]:
                dp[j]=max(dp[j],dp[j-w[i]]+val[i])
            j-=1
    print(dp[t])

