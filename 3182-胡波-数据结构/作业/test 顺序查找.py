# coding:gbk
import random

'''val = 0
data = [0] * 80
for i in range(80):
    data[i] = random.randint(1,150)
while val != -1:
    find = 0
    val = int(input('请输入查找键值(1-150)，输入-1离开：'))
    for i in range(80):
        if data[i] == val:
            print('在第%3d个位置找到键值 [%3d]'%(i+1,data[i]))
            find += 1
    if find == 0 and val != -1:
        print('######没有找到[%3d]######' % val)
print('数据内容为：')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]'%(i*8+j+1,data[i*8+j]),end='')
    print('')'''

val = 0
data = [23,32,45,67,89,90,289,2349]
while val != -1:
    find = 0
    val = int(input('请输入查找键值(1-150)，输入-1离开：'))
    for i in range(80):
        if data[i] == val:
            print('在第%3d个位置找到键值 [%3d]'%(i+1,data[i]))
            find += 1
    if find == 0 and val != -1:
        print('######没有找到[%3d]######' % val)
print('数据内容为：')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]'%(i*8+j+1,data[i*8+j]),end='')
    print('')

'''def sequentialSearchUnorder(alist,item):
    found= False
    post=0
    while not found and post<len(alist):
        if alist[post]==item:
            found=True
            print(item,'在',post+1,'位上')
        else:
            post=post+1
            # print("not found")
    return found
print(sequentialSearchUnorder([1,52,6,3,9,11,488,56,54,2,4,6,7,89],89))

'''