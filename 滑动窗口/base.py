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
"""
i 指针表示窗口左边界，j 指针表示窗口右边界。
当 sum < target 时，j 指针右移。
当 sum > target 时，i 指针右移。
当 sum = target 时，窗口内的数组加入 res，i 指针右移。
注意窗口的 range 是左闭右开 [ )。
时间复杂度: O(n)
i每次右移，sum要减去对应之前的i值，这样一旦sum>target 或者等于，就可以通过调整i的位置，不断寻找合适的列表。
"""
class Solution(object):
    def findContinuousSequence(self, target):
        i, j = 1, 1
        sum = 0
        res = []

        while i <= target // 2:
            if sum < target:
                # j + 1
                sum += j
                j += 1
            elif sum > target:
                # i + 1
                sum -= i
                i += 1
            else:
                arr = list(range(i, j))
                res.append(arr)
                # i + 1
                sum -= i
                i += 1

        return res
t1=Solution()
print(t1.findContinuousSequence(9))