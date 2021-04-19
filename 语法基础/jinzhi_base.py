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

# str=input()
# print(int(str,16))
# a=int(str,16)
# print("{:0b}-666".format(a,2))
# print("{:0o}".format(a))
# print("{:0x}".format(a))#X




def baseN(num, b):
    if num==0:
        return "0"
    else:
        return (baseN(num // b, b).lstrip("0") + "0123456789ABCDEFghijklmnopqrstuvwxyz"[num % b])
    #注意.lstrip("0") 记住就完了 就结合短除法理解下这个递归过程
    #return ((num == 0) and "0") or (baseN(num // b, b).lstrip("0") + "0123456789ABCDEFghijklmnopqrstuvwxyz"[num % b])

if __name__=="__main__":
    # n=int(input().strip())
    # str1=input().strip()
    # m=int(input().strip())
    # temp=int(str1,n)
    # print(baseN(temp,m))
    print(baseN(0,16))

