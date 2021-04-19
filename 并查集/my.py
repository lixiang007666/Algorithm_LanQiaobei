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

class my:
    def __init__(self,n):
        self.makeset(n)
    def makeset(self,n):
        self.s=[i for i in range(1,n+1)]
    def sameset(self,x,y):
        return self.find(x)==self.find(y)
    def find(self,x):
        if x==self.s[x-1]:
            return x
        else:
            return self.find(self.s[x-1])
    def union(self,x,y):
        rootx,rooty=self.find(x),self.find(y)
        self.s[rootx-1]=rooty

if __name__=="__main__":
    n, m, p = list(map(int, input().strip().split()))
    t1 = my(n)
    for i in range(m):
        x, y = list(map(int, input().strip().split()))
        t1.union(x, y)
    for i in range(p):
        a,b=list(map(int,input().strip().split()))
        if t1.sameset(a,b):
            print("Yes")
        else:
            print("No")