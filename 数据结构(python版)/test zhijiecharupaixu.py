# coding:gbk

lis = input('\n请输入十个正整数：')#版本的需要使用raw_input输入
arrays=[int(a) for a in lis.split()]    #将输入每个数以空格键隔开做成数组
print("输入的十个整数为：") 
print(arrays)                          
for a in range(len(arrays)):            #取arrays的长度做为循环条件
    for b in range(len(arrays)-1):      #取arrays-1的长度做为循环条件
        if arrays[b] > arrays[b+1]:      #如果数组中的第一个值大于第二个值
            temp = arrays[b]             #则将大的值arrays[b]赋值在temp中
            arrays[b] = arrays[b+1]      #将小的值arrays[b+1]赋值在第一个值中
            arrays[b+1] = temp           #将temp中的值赋值在第二个值中，实现更换位置
    print("\n第%d" % (a + 1) + "次排序为：")
    for c in range(len(arrays)):        #循环获取数组的长度
        print(arrays[c])               #打印排序的过程
print("\n最终的排序为：")
for c in arrays:                        #循环获取数组长度
    print(str(c))                       #打印最终的排序结果，输

# L = [1, 3, 2, 32, 15, 5, 4]
# def Insert_sort(L):
#     for i in range(1,len(L)):
#         for j in range(0,i):#这里面其实也是从前向后比较
#             if L[i]<L[j]:
#                 L.insert(j,L[i])#在不大于的位置插入L[i],这个时候，列表加长了1位,L[i]插入到指定位置了，但它的值也向后移动了一位
#                 L.pop(i+1)#把原来L[i]的值删除。
#     print(L)
#     #空间复杂度为O（1），时间复杂度为O（n*n）
# Insert_sort(L)
# # print sorted(L)#自带的两种排序
