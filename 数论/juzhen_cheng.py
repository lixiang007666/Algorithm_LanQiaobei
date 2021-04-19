"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866

"""
m,s,n=list(map(int,input().split(" ")))
mar1=[]
mar2=[]
for i in range(m):
    mar1.append(list(map(int,input().split())))
for i in range(s):
    mar2.append(list(map(int,input().split())))
def mul(x1,x2):
    c=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(s):
                c[i][j]+=x1[i][k]*x2[k][j]#  += +=
    return c
res=mul(mar1,mar2)
for i in range(m):
    for j in range(n):
        print(res[i][j],end=" ")
    print("")

