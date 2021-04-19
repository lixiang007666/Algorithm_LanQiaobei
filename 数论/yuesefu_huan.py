"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866
f(1)=0；//递归出口
f(n)=[f(n-1)+m]%n；//递归体
"""
def fun(n,M):
   if n==1:
      return 0
   else:
      return (fun(n-1,M)+M)%n

M=3
n=int(input())
s=0
for i in range(2,n+1):
   s=(s+M)%i
print(s+1)
print(fun(n,M)+1)



