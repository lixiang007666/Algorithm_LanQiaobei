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

#goods=[(60,10),(100,20),(120,30)]# 每个商品元祖表示（价格，重量）
#goods.sort(key=lambda x: x[0] / x[1], reverse=True)

def fun(goods,w):
    #print(goods)
    m=[0 for _ in range(len(goods))]
    for i,(price,weight) in enumerate(goods):
        if w>=weight:
            m[i]=1
            w-=weight
        else:
            m[i]=w/weight
            w=0
            break#不用迭代到最后一个
    return m


if __name__=="__main__":
    goods=[]
    for i in range(3):
        x,y=list(map(int,input().split()))
        goods.append((x,y))
    print(goods)
    goods.sort(key=lambda x: x[0] / x[1], reverse=True)#！！！！！！
    print(fun(goods, 50))