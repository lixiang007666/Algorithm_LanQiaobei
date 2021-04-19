list1=[1,2,2,2,3]
d={}
for i in list1:
    d[i]=d.get(i,0)+1
print(d)

print(d.items())
print(d.keys())
print(d.values())
d=sorted(d.items(),key=lambda x:x[1],reverse=True)
print(d)

