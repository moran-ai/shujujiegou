# coding:gbk

lis = input('\n������ʮ����������')#�汾����Ҫʹ��raw_input����
arrays=[int(a) for a in lis.split()]    #������ÿ�����Կո��������������
print("�����ʮ������Ϊ��") 
print(arrays)                          
for a in range(len(arrays)):            #ȡarrays�ĳ�����Ϊѭ������
    for b in range(len(arrays)-1):      #ȡarrays-1�ĳ�����Ϊѭ������
        if arrays[b] > arrays[b+1]:      #��������еĵ�һ��ֵ���ڵڶ���ֵ
            temp = arrays[b]             #�򽫴��ֵarrays[b]��ֵ��temp��
            arrays[b] = arrays[b+1]      #��С��ֵarrays[b+1]��ֵ�ڵ�һ��ֵ��
            arrays[b+1] = temp           #��temp�е�ֵ��ֵ�ڵڶ���ֵ�У�ʵ�ָ���λ��
    print("\n��%d" % (a + 1) + "������Ϊ��")
    for c in range(len(arrays)):        #ѭ����ȡ����ĳ���
        print(arrays[c])               #��ӡ����Ĺ���
print("\n���յ�����Ϊ��")
for c in arrays:                        #ѭ����ȡ���鳤��
    print(str(c))                       #��ӡ���յ�����������

# L = [1, 3, 2, 32, 15, 5, 4]
# def Insert_sort(L):
#     for i in range(1,len(L)):
#         for j in range(0,i):#��������ʵҲ�Ǵ�ǰ���Ƚ�
#             if L[i]<L[j]:
#                 L.insert(j,L[i])#�ڲ����ڵ�λ�ò���L[i],���ʱ���б�ӳ���1λ,L[i]���뵽ָ��λ���ˣ�������ֵҲ����ƶ���һλ
#                 L.pop(i+1)#��ԭ��L[i]��ֵɾ����
#     print(L)
#     #�ռ临�Ӷ�ΪO��1����ʱ�临�Ӷ�ΪO��n*n��
# Insert_sort(L)
# # print sorted(L)#�Դ�����������
