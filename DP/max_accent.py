

if __name__=="__main__":
    b=[0 for i in range(3)]
    b[0]=1
    len=0
    a=list(map(int,input().split()))
    for i in range(3):
        for k in range(0,i):
            len=max(b[0:k+1])
            if a[i]>a[k]:
                b[i]=len+1
    print(max(b))

# xxxxxxxxx