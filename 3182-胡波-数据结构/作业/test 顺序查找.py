# coding:gbk
import random

'''val = 0
data = [0] * 80
for i in range(80):
    data[i] = random.randint(1,150)
while val != -1:
    find = 0
    val = int(input('��������Ҽ�ֵ(1-150)������-1�뿪��'))
    for i in range(80):
        if data[i] == val:
            print('�ڵ�%3d��λ���ҵ���ֵ [%3d]'%(i+1,data[i]))
            find += 1
    if find == 0 and val != -1:
        print('######û���ҵ�[%3d]######' % val)
print('��������Ϊ��')
for i in range(10):
    for j in range(8):
        print('%2d[%3d]'%(i*8+j+1,data[i*8+j]),end='')
    print('')'''

val = 0
data = [23,32,45,67,89,90,289,2349]
while val != -1:
    find = 0
    val = int(input('��������Ҽ�ֵ(1-150)������-1�뿪��'))
    for i in range(80):
        if data[i] == val:
            print('�ڵ�%3d��λ���ҵ���ֵ [%3d]'%(i+1,data[i]))
            find += 1
    if find == 0 and val != -1:
        print('######û���ҵ�[%3d]######' % val)
print('��������Ϊ��')
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
            print(item,'��',post+1,'λ��')
        else:
            post=post+1
            # print("not found")
    return found
print(sequentialSearchUnorder([1,52,6,3,9,11,488,56,54,2,4,6,7,89],89))

'''