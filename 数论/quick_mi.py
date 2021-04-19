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


def power(base,exponent):
    res = 1
    while exponent:
        if exponent & 1:  # 判断当前的最后一位是否为1，如果为1的话，就需要把之前的幂乘到结果中。
            res *= base
        base *= base  # 一直累乘，如果最后一位不是1的话，就不用了把这个值乘到结果中，但是还是要乘。
        exponent = exponent >> 1
    return res

power()

import math
import cmath
import sys
import string
import heapq
import bisect
import copy
from queue import Queue, PriorityQueue, LifoQueue
from collections import Counter, deque
from itertools import permutations, combinations
from functools import cmp_to_key, reduce


# def quick(base, exp):
#     res = 1
#     while exp:
#         if exp & 1:
#             res = (res * base)%100003
#             base = (base * base)%100003
#         exp = exp >> 1
#     return res
#
#
# if __name__ == "__main__":
#     m, n = list(map(int, input().strip().split()))
#     # print(gcd(15,6))
#     h = quick(m, n)
#     k = quick(m - 1, n - 1)
#     print((h % 100003 - (m * k) % 100003 + 100003) % 100003)