def rec_subset(arr, i, s):
    if s == 0:
        return True
    elif i == 0:
        return arr[0] == s
    elif arr[i] > s:
        return rec_subset(arr, i - 1, s)
    else:
        A = rec_subset(arr, i - 1, s - arr[i])#选
        B = rec_subset(arr, i - 1, s)#不选
        return A or B



if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    print(rec_subset(arr, len(arr) - 1, 9))


