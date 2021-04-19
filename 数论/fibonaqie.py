import math
import cmath
import string
import sys
import bisect
import ctypes
from queue import Queue, LifoQueue, PriorityQueue
from itertools import permutations, combinations
from collections import deque, Counter


def fun(n):
    fst = 1  # 爬到1楼只有1种方法
    scd = 2  # 爬到2楼有两种方法
    thd = 4
    res = 0  # 初始化爬到n楼的方法
    for i in range(3, n):  # 从3楼开始算
        res = fst + scd + thd
        fst = scd  # 推导下一层
        scd = thd
        thd = res

    return max(n, res)  # 返回n和res中较大的那个


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        x = int(input())
        if x == 3:
            print(4)
        else:
            print(fun(x))







