"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866

"""
import math as mt
import string
while True:
    try:
        def gcd(a,b):
            if a%b==0:
                return b
            else:
                return gcd(b,a%b)
        n,m=list(map(int,input().split()))
        temp=gcd(n,m)
        print("{:.0f}".format(n*m/temp))
    except:
        break

