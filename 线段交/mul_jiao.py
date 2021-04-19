"""
@Author:Lixiang

@Blog(个人博客地址): https://lixiang007.top/

@WeChat：18845312866

"""
while True:
    try:
        s1 = list(map(float, input().split()))
        s2 = list(map(float, input().split()))
        if s1[0] > s1[2]:
            s1[0],s1[2] = s1[2],s1[0]
        if s1[1] > s1[3]:
            s1[1], s1[3] = s1[3], s1[1]
        if s2[0] > s2[2]:
            s2[0],s2[2] = s2[2],s2[0]
        if s2[1] > s2[3]:
            s2[1],s2[3] = s2[3],s2[1]
        temp_x1 = max(s1[0],s2[0])
        temp_x2 = min(s1[2],s2[2])
        temp_y1 = max(s1[1],s2[1])
        temp_y2 = min(s1[3],s2[3])
        if temp_x2-temp_x1<0 or temp_y2-temp_y1<0:
            res = 0
        else:
            res = (temp_y2-temp_y1)*(temp_x2-temp_x1)
        print("{:.2f}".format(res))
    except:
        break

