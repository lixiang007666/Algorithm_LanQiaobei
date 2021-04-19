import sys
import math
import cmath
import bisect
import string
import heapq
from itertools import combinations, permutations
from collections import Counter, deque
from queue import LifoQueue, Queue, PriorityQueue
from functools import cmp_to_key


def bisect_fun(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2
        if x < a[mid]:
            right = mid - 1
        elif x > a[mid]:
            left = mid + 1
        else:
            return True
    return False


if __name__ == "__main__":
    a = [5, 4, 645, 2, 78, 76, 68, 223, 98]
    a.sort()
    print(bisect_fun(a, 15))
    print(bisect_fun(a, 5))
    print(bisect_fun(a, 223))
    print(bisect_fun(a, 800))





