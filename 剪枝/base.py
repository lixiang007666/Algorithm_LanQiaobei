import copy
import math
import cmath
import sys
import string
import bisect
import heapq
from queue import Queue,LifoQueue,PriorityQueue
from itertools import combinations,permutations
from collections import Counter,deque
from functools import cmp_to_key

reslist=[]
valuelist=[]
def dfs(candidates,target,count):
    if target==0:
        reslist.append(copy.deepcopy(valuelist))
        return
    for i in range(count,len(candidates)):
        if candidates[i]<=target:
            valuelist.append(candidates[i])
            dfs(candidates,target-candidates[i],i)
            valuelist.pop()

if __name__=="__main__":
    dfs([2,3,6,7],7,0)
    print(reslist)
