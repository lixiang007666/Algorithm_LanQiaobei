



def chess(tr, tc, pr, pc, size):  # tr:棋盘初始行号 tc:棋盘初始列号
# pr:特殊棋盘格行号 pc:特殊棋盘格列号
# size:棋盘格大小
    global mark
    global table
    if size == 1:
        return  # 递归终止条件
    mark += 1  # 表示直角骨牌号
    count = mark
    half = size // 2  # 当size不等于1时，棋盘格规模减半，变为4个

# 小棋盘格进行递归操作
# 左上角
    if (pr < tr + half) and (pc < tc + half):
        chess(tr, tc, pr, pc, half)
    else:
        table[tr + half - 1][tc + half - 1] = count
        chess(tr, tc, tr + half - 1, tc + half - 1, half)#根据tr和tc得到特殊格子位置
# 将[tr+half-1,tc+half-1]作为小规模棋盘格的特殊点，进行递归

# 右上角
    if (pr < tr + half) and (pc >= tc + half):
         chess(tr, tc + half, pr, pc, half)
    else:
         table[tr + half - 1][tc + half] = count
         chess(tr, tc + half, tr + half - 1, tc + half, half)
# 将[tr+half-1,tc+half]作为小规模棋盘格的特殊点，进行递归

# 左下角
    if (pr >= tr + half) and (pc < tc + half):
         chess(tr + half, tc, pr, pc, half)
    else:
         table[tr + half][tc + half - 1] = count
         chess(tr + half, tc, tr + half, tc + half - 1, half)
# 将[tr+half,tc+half-1]作为小规模棋盘格的特殊点，进行递归

# 右下角
    if (pr >= tr + half) and (pc >= tc + half):
        chess(tr + half, tc + half, pr, pc, half)
    else:
        table[tr + half][tc + half] = count
        chess(tr + half, tc + half, tr + half, tc + half, half)
# 将[tr+half,tc+half]作为小规模棋盘格的特殊点，进行递归

# 输出矩阵
def show(table):
    n = len(table)
    for i in range(n):
        for j in range(n):
            print(table[i][j], end='	')
        print('')


mark = 0
n = 8  # 输入8*8的棋盘规格
table = [[-1 for x in range(n)] for y in range(n)]  # -1代表特殊格子
chess(0, 0, 2, 2, n)  # 特殊棋盘位置
show(table)