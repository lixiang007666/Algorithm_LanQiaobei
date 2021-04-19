from itertools import combinations,permutations


s=[1,2,3]
list1=list(permutations(s,3))
print(list1)
list2=list(permutations(s,2))
print(list2)
list3=list(combinations(s,2))
print(list3)

seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
    print(i, element)
a=[1,2,3]
b=[7,8,9]
print(list(zip(a,b)))
zipped=[(1,4),(2,5),(3,6)]
print(list(zip(*zipped)))#加一个* 一个数组

