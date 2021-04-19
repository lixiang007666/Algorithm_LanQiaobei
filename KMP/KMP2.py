import sys
#统计次数
# 1
# AZA
# AZAZAZA
# [-1, 0, 0, 1]
# 3
def get_next(s):
    i = 0
    j = -1
    next = [-1]
    while i < len(s):
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            next.append(j)
        else:
            j = next[j]
    print(next)
    return next


def kmp(s1, s2):
    count = 0
    next = get_next(s2)
    i = 0
    j = 0
    while i < len(s1):
        if j == -1 or s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            j = next[j]
        if j == len(s2):
            count += 1
            j = next[j]
    return count


if __name__ == "__main__":
    n = int(input())
    while n:
        x = input()
        y = input()
        ans = kmp(y, x)
        print(ans)
        n -= 1

