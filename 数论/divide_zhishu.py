"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866

"""
while True:
    try:
        def zhishufenjie(res, n, result):  #res是存储分解质因数的式子，n是当前被分解的数
            for i in range(2, n + 1):
                if n % i == 0:   #如果n能整除i
                    res += str(i)
                    n = n // i
                    if n == 1:
                        return res
                    elif n in result.keys():   #走捷径，假如我们判断36，判断一次到18了，18之前做过了，直接拿过来hhhhhhh
                        res += '*'
                        res += result[n]
                        return res
                    else:
                        res += '*'
                        return zhishufenjie(res, n, result)

        min_num, max_num = map(int, input().split())
        result = {}   #result是存储值与其分解质因数的对应关系
        for num in range(min_num,max_num + 1):
            res = ''
            result[num] = zhishufenjie(res,num,result)#！！！！！！！！！
        for k,v in result.items():
            s = str(k)+'='+str(v)
            print(s)
    except:
        break


"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866

"""
import math
import string
import sys
import cmath
from itertools import permutations
def fun(n,res):
    for i in range(2,n+1):
        if n %i==0:
            res+=str(i)
            n=n//i
            if n==1:#短除到质数退出
                return res
            else:
                res+='*'
                return fun(n,res)
n=int(input())
res=""
temp=fun(n,res)
print(n,"=",temp,sep="")

