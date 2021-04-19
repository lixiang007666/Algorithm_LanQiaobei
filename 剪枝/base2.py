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
from functools import cmp_to_key,reduce

reslist=[]
valuelist=[]
def dfs(candidates,target,count):
    if target==0:
        reslist.append(copy.deepcopy(valuelist))
        return
    for i in range(count,len(candidates)):
        if candidates[i]<=target:
            #剪枝！！！！！！！！！！！！！！！！！！！！！！！！
            if i>count and candidates[i]==candidates[i-1]: #保证i-1存在!!!!!!!!!!!!!!!
                continue
            valuelist.append(candidates[i])
            dfs(candidates,target-candidates[i],i+1)
            valuelist.pop()

if __name__=="__main__":
    can=[10,1,2,7,6,1,5]
    can.sort()
    dfs(can,8,0)
    print(reslist)
