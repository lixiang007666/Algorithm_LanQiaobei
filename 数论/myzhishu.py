

res=[]

def zhishufenjie(n):

    for i in range(2,n+1):
        if n%i==0:
            res.append(i)
            n=n//i
            if n==1:
                return
            else:
                return zhishufenjie(n)

if __name__=="__main__":
    n = int(input())
    zhishufenjie(n)
    print(res)