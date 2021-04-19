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

dp=[[0 for _ in range(25)] for _ in range(25)]
s=[[0 for _ in range(25)] for _ in range(25)]
fx=[0, -2, -1, 1, 2, 2, 1, -1, -2]
fy=[0, 1, 2, 2, 1, -1, -2, -2, -1]

if __name__=="__main__":
    bx,by,mx,my=list(map(int,input().strip().split()))
    bx+=2
    by+=2
    mx+=2
    my+=2
    s[mx][my]=1
    dp[2][2]=1
    for i in range(1,9):
        s[mx+fx[i]][my+fy[i]]=1
    for i in range(2,bx+1):
        for j in range(2,by+1):
            if s[i][j]:
                continue
            dp[i][j]=max(dp[i][j],dp[i-1][j]+dp[i][j-1])
    #print(dp)
    print(dp[bx][by])
    #其中每个点的值代表的是当前这个点会有几条路径用过这个点（路径指的是从A到B的路径）
    # f[1][1] = 1
    # f[i][j] = f[i−1][j] + f[i][j−1]
    # 但是这个方程是推不出结果的, 因为这样
    # A
    # 点会在一开始的时候被覆盖成
    # 0
    # 所以修改以后的方程就是
    # f[1][1] = 1
    # f[i][j] = max(f[i−1][j] + f[i][j−1], f[i][j])
