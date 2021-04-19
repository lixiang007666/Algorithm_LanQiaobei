import copy

a=[1,2]
b=[1,2]
c=a
d=copy.deepcopy(b)
c.pop()
d.pop()
print(a)
print(b)
