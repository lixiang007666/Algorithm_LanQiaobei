#要求数字不相连
def rec_opt(arr ,i):
    if i== 0:
        return arr[0]
    elif i == 1:
        return max(arr[0], arr[1])
    else:
        A = rec_opt(arr, i - 2) + arr[i]#选
        B = rec_opt(arr, i - 1)#不选
        return max(A, B)


def dp_opt(arr):
    opt = [0 for i in range(len(arr))]
    opt[0] = arr[0]
    opt[1] = max(arr[0], arr[1])
    for i in range(2, len(arr)):
        A = opt[i - 2] + arr[i]
        B = opt[i - 1]
        opt[i] = max(A, B)
    return opt[len(arr) - 1]


if __name__ == "__main__":
    arr = [1, 2, 4, 1, 7, 8, 3]
    print(rec_opt(arr, 6))
    print(dp_opt(arr))



