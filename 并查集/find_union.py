import math
import cmath
import string
import sys
import bisect
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from itertools import permutations,combinations
from collections import deque,Counter
from functools import cmp_to_key

class find_union:
    def __init__(self,n):
        self.makeset(n)
    def makeset(self,n):
        self.S=[i for i in range(1,n+1)]#祖先数组
    def find(self,x):#查祖先
        if x==self.S[x-1]:
            return x
        else:
            return self.find(self.S[x-1])
    def union(self,x,y):
        rootx,rooty=self.find(x),self.find(y)
        self.S[rootx-1]=rooty
    def sameset(self,x,y):
        return self.find(x)==self.find(y)
    def count(self):
        sum=0
        for i in range(len(self.S)):
            if (i+1)==self.S[i]:
                sum+=1
        return sum

if __name__=="__main__":
    n,m=list(map(int,input().strip().split()))
    t1=find_union(n)
    sum=0
    for i in range(m):
        x,y=list(map(int,input().strip().split()))
        t1.union(x,y)
    print(t1.count())


