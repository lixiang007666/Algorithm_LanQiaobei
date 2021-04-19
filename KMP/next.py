# 然后这里说一下找周期前缀，如aabaabaabaab，当前缀长度为2,6,9,12时，前缀为周期字符串，
# 可以直接用找next数组的办法找，先自匹配，找到错位部分，如果剩余部分的长度是错位部分的整数倍，那么就是一个周期字符串。
# 其实就是对KMP算法中的next数组的使用，假设next[j] = k
#
# 那么如果是周期字符串有：j % (j - k)余数为0那么认为这个字符串是周期性的，而且重复的次数：j / (j - k)
# Sample Input
# 3
# aaa
# 12
# aabaabaabaab
# 0
# Sample Output
# Test case #1
# 2 2
# 3 3
#
# Test case #2
# 2 2
# 6 2
# 9 3
# 12 4

def Gen_next(str):
    j=-1
    i=0
    next=[-1]
    while i<len(str):
        if j==-1 or str[i]==str[j]:
            i+=1
            j+=1
            next.append(j)
        else:
            j=next[j]
    print(next)
    return next


if __name__=="__main__":
    next=Gen_next("aaa")
    a=next[1:]
    print(a)
    for i in range(1,len(a)):
        if a[i]==0: #到这为止肯定不是周期子串
            continue
        if (i+1)%(i+1-a[i])==0:
            print(i+1,(i+1)//(i+1-a[i]))