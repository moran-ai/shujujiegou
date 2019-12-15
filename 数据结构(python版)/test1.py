# length = 12
# width = 45
# s = length*width
# print(s)

# len = int(input("输入长度:"))
# width = int(input("输入宽度:"))
# area = len * width
# print(area)
#
# from math import *
# # 三角形的面积
# a = int(input("输入第一条边:"))
# b = int(input("输入第二条边:"))
# c = int(input("输入第三条边:"))
#
# if a +b >c or  a + c >b or  b + c >a:
#     p = (a+ b+ c)/2
#     s = sqrt((p-a)*(p-b)*(p-c)*p)
#     print(s)
# else:
#     print('bu man zu')
#

# 百钱买百鸡算法
for x in range(1,21):
    for y in range(1,34):
        z = 100-(x+y)
        if z%3 ==0 and 5*x+3*y+z/3 ==100:
            print('母鸡:%d只,公鸡:%d只,小鸡:%d只'%(x,y,z))

