import math
import cmath
import sys
import string
import heapq
import bisect
import copy
from queue import Queue,PriorityQueue,LifoQueue
from collections import Counter,deque
from itertools import permutations,combinations
from functools import cmp_to_key,reduce

#给出一个字符串，求在其尾部需要加几个字符使其构成循环节
# 首先，求出所给字符串的next数组，然后判断字符串数组长度与next数组最后一个值的差值与n的关系：
# 是否等于n以及是否为n的约数，如果不是则所需加字符数量为零，如果是所加字符数量为差值减去n与差值的余数。

def Gen_next(str):
    j=-1
    i=0
    next=[-1]
    while i<len(str):
        if j==-1 or str[i]==str[j]:
            i+=1
            j+=1
            next.append(j)
        else:
            j=next[j]
    return next


if __name__=="__main__":
    s=input()
    next=Gen_next(s)
    j=len(s)
    a=next[1:]
    k=a[-1]
    if j%(j-k)==0 and (j-k)!=len(s):
        print(0)
    else:
        #要补的字符个数=l-n%l    l是循环节长度 n是字符串长度
        #可以将n%l理解为已经有的长度 l为目标长度 那么l-（n%l） 就是要补的长度
        l=j-k
        print(l-len(s)%l)


