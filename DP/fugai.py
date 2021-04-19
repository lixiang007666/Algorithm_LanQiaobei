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

heights=[]
maxheight=[[0 for i in range(105)] for _ in range(105)]
dp=[[0 for i in range(105)] for _ in range(105)]

if __name__=="__main__":
    n,m=list(map(int,input().strip().split()))
    heights.append(0)
    heights.extend(list(map(int,input().strip().split())))
    #print(heights)
    for i in range(1,n+1):
        maxheight[i][i]=heights[i]
        for j in range(i+1,n+1):
            maxheight[i][j]=max(maxheight[i][j-1],heights[j])
    for i in range(1,n+1):
        dp[i][1]=i*maxheight[1][i]
        j=2
        while j<=i and j<=m:
            dp[i][j]=math.inf
            for k in range(1,i-j+2):
                dp[i][j]=min(dp[i][j],dp[i-k][j-1]+k*maxheight[i-k+1][i])
            j+=1
    print(dp[n][m])




