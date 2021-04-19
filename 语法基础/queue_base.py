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
#Queue 和 LifoQueue同理哦
pq=PriorityQueue()
pq2=PriorityQueue(maxsize=6)
pq.put(1)
pq.put(5)
pq.put(3)
i=0
print(pq.empty())
print(pq.queue)
while i<pq.qsize():
    print(pq.get(),end=" ")
print("")
print(pq.full())
print(pq.empty())

q = PriorityQueue()

# 格式：q.put((数字,值))
#特点：数字越小，优先级越高
q.put((1,'lori'))
q.put((-1,'Jseon'))
q.put((10,'King'))
i = 0
while i<q.qsize():
    print(q.get()[1])



if __name__=="__main__":
    n=int(input())
    m=list(map(int,input().strip().split()))
    q1=PriorityQueue()
    for i in m:
        q1.put(i)
    s=0
    while q1.qsize()>1:
        a=q1.get()
        b=q1.get()
        s+=a+b
        q1.put(a+b)
    print(s)


# Huffuman树 zhijie
x = int(input())
if x >= 0 & x <= 100:
    list1 = list(map(int, input().split()))
    list1.sort(reverse=True)
    while list1[0] > 1000:
        del(list1[0])
    total = 0
    while len(list1) > 1:
        list1.sort(reverse=True)
        num = list1.pop()+list1.pop()
        total = total + num
        list1.append(num)
    print(total)



