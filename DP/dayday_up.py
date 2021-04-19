import math
import cmath
import string
import sys
import bisect
import heapq
from queue import Queue, LifoQueue, PriorityQueue
from itertools import permutations, combinations
from collections import deque, Counter
from functools import cmp_to_key

if __name__ == "__main__":
    dp = [[0 for _ in range(2005)] for _ in range(2005)]
    n = int(input())
    a = list(map(int, input().strip().split()))
    ans = 0
    i = n - 1
    while i >= 0:
        dp[i][1] = 1
        for j in range(i + 1, n):#比i大1
            if a[j] > a[i]:
                k = 2# 长度
                while 1:
                    if dp[j][k - 1] == 0:
                        break
                    dp[i][k] = dp[i][k] + dp[j][k - 1]
                    k += 1
        i -= 1
    for i in range(n):
        ans += dp[i][4]
    print(ans)



