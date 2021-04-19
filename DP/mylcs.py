import math
import cmath
import string
import sys
import bisect
import copy
import heapq
from queue import Queue,PriorityQueue,LifoQueue
from itertools import permutations,combinations
from functools import cmp_to_key,reduce
from collections import deque,Counter

def lcs(x,y):
    n=len(x)
    m=len(y)
    c=[[0 for _ in range(m+1)] for _ in range(n+1)]
    b = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]=1
            else:
                if c[i-1][j]>=c[i][j-1]:
                    c[i][j]=c[i-1][j]
                    b[i][j] = 2
                else:
                    c[i][j]=c[i][j-1]
                    b[i][j] = 3
    return c[n][m],b



def lcs_traceback(x,y):
    c,b=lcs("ABCDAB","ACD")
    i=len(x)
    j=len(y)
    res=[]
    while i>0 and j>0:
        if b[i][j]==1:
            res.append(x[i-1])
            i-=1
            j-=1
        elif b[i][j]==2:
            i-=1
        else:
            j-=1
    return "".join(reversed(res))



if __name__=="__main__":
    print(lcs_traceback("ABCDAB","ACD"))
