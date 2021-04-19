"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866

"""
import math as mt
import string
"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866

"""
import math as mt
import string
# while True:
#     try:
#         n = int(input())
#         s = set()
#         ans = 1
#         def sushu(n):
#             for i in range(2,n+1):
#                 if n%i == 0:
#                     s.add(i)#s.remove（i）
#                     n = n//i
#                     if n==1:
#                         return
#                     else:
#                         return sushu(n)
#
#         sushu(n)
#         for num in s:
#             ans *= num
#         print(ans)
#     except:
#         break



"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866

"""
import math
import string
import sys
from itertools import permutations
import cmath
res=[]
def zhishufenjie(n):  #res是存储分解质因数的式子，n是当前被分解的数
    for i in range(2,n+1):
        if n%i==0:
            res.append(i)
            n=n//i
            if n==1:
                return
            else:
                return zhishufenjie(n)
n=int(input())
zhishufenjie(n)
for i in res:
    print(i,end=" ")
print("")
print(len(res))
