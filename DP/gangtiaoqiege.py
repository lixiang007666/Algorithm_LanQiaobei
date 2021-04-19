import sys
import math
import cmath
import string
import bisect
from itertools import permutations, combinations
from queue import Queue, PriorityQueue, LifoQueue
from collections import Counter, deque
from functools import cmp_to_key

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]

#cut_rod_recurision(p, n)表示rn
def cut_rod_recurision(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n):
            res = max(res, cut_rod_recurision(p, i) + cut_rod_recurision(p, n - i))
        return res


#从钢条左侧切割长度为i的一段 右侧继续切割
def cut_rod_recurision2(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recurision2(p, n - i))#得有一个res做比较
        return res


def cut_rod_dp(p, n):
    #重叠子问题处理
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]

def cut_rod_extend(p,n):
    r=[0]
    s=[0]
    for i in range(1,n+1):
        res_r=0
        res_s=0
        for j in range(1,i+1):
            if p[j]+p[i-j]>res_r:
                res_r=p[j]+p[i-j]
                res_s=j
        r.append(res_r)
        s.append(res_s)
    return r[n],s

#可以理解为对列表反向推到的过程
#通过一个记录其他信息的表 往回追答案 动态规划很常见
def cut_rod_solution(p,n):
    r,s=cut_rod_extend(p,n)
    ans=[]
    while n>0:
        ans.append(s[n])
        n-=s[n]
    return ans

if __name__ == "__main__":
    print(cut_rod_recurision(p, 9))
    print(cut_rod_recurision2(p, 9))
    print(cut_rod_dp(p, 9))
    print(cut_rod_extend(p, 9))
    print(cut_rod_solution(p, 9))

