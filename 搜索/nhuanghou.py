count=0
# 检测（x,y）这个位置是否合法（不会被其他皇后攻击到）
def is_attack(queue, x, y):
    for i in range(x):
        if queue[i] == y or abs(x - i) == abs(queue[i] - y):
            return True
    return False


# 按h来摆放皇后
def put_position(n, queue, row):
    global count
    for i in range(n):
        if not is_attack(queue, row, i):
            queue[row] = i
            if row == n - 1:  # 此时最后一个皇后摆放好了，打印结果。
                count+=1
                print(queue)
            else:
                put_position(n, queue, row + 1)
    #到这自己就回溯了 不用写return 无路可走和找到一种答案都回溯

n = 4
queue = [0 for i in range(n)]
put_position(n, queue, 0)
print(str(count)+"种方案")

# [1, 3, 0, 2]
# [2, 0, 3, 1]