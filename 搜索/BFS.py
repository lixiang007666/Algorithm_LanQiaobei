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
#腐烂的橘子
class Solution(object):
    def orangeRotting(self,grid):
        x,y,time=len(grid),len(grid[0]),0
        for _ in grid:
            print(_)
        locs=[[1,0],[0,-1],[-1,0],[0,1]]
        queue=[]
        for i in range(x):
            for j in range(y):
                if grid[i][j]==2:
                    queue.append((i,j,time))
        while queue:
            loc_x,loc_y,time=queue.pop(0)
            for loc in locs:
                af_x=loc_x+loc[0]
                af_y=loc_y+loc[1]
                if 0<=af_x<x and 0<=af_y<y and grid[af_x][af_y]==1:
                    grid[af_x][af_y]=2
                    queue.append((af_x,af_y,time+1))
        for row in grid:
            if 1 in row:
                return -1
        return time

if __name__=="__main__":
    t1=Solution()
    print(t1.orangeRotting([[2,1,1],[1,1,0],[0,1,1]]))
    print(t1.orangeRotting([[0,2]]))
    print(t1.orangeRotting([[2,1,1],[0,1,1],[1,0,1]]))



