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

flag=0
vis=[0 for i in range(6)]
m=[[0 for i in range(6)] for j in range(6)]

def dfs(num):
    global flag
    if num==6:
        flag=1
        return
    else:
        for j in range(6):
            if not vis[num] and m[num][j]==1:
                vis[num]=1
                dfs(num+1)
                vis[num]=0


if __name__=="__main__":
    t=int(input())
    while t:
        flag=0
        vis=[0 for i in range(6)]
        m=[[0 for i in range(6)] for j in range(6)]
        for i in range(6):
            s=input().strip()
            for j in range(len(s)):
                if s[j]=="h":
                    m[i][0]=1
                if s[j]=="a":
                    m[i][1]=1
                if s[j]=="r":
                    m[i][2]=1
                if s[j]=="b":
                    m[i][3]=1
                if s[j]=="i":
                    m[i][4]=1
                if s[j]=="n":
                    m[i][5]=1
        dfs(0)
        if flag:
            print("Yes")
        else:
            print("No")
        t-=1