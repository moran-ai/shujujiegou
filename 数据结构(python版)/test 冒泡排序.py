# coding:gbk
##################################
class ListItem(object):
    def __init__(self ,key,value):
        self.key = key
        self.value = value
class SortSequenceList(object):
    def __init__(self):
        self.SeqList=[]
    def  CreateSequenceListByInput(self,nElement):
        self.SeqList.append(ListItem(int(0), 0))
        print("���������ݣ�")
        for i in range(1,nElement+1):
            a = input()
            self.SeqList.append(ListItem(int(a), i))
    def TraverseElementSet(self):
        for i in range(1,len(self.SeqList)):
            print(self.SeqList[i].key)

    ########################
    #�㷨8-7 ð�������㷨
    ########################
    def BubbleSort(self):
        SeqListLen = len(self.SeqList)
        for i in range(1,SeqListLen-1):
            for j in range(1,SeqListLen-i):
                print("j=",j)
                if self.SeqList[j+1].key < self.SeqList[j].key:
                    self.SeqList[0].key = self.SeqList[j].key
                    self.SeqList[j].key = self.SeqList[j+1].key
                    self.SeqList[j+1].key = self.SeqList[0].key
                #     print("'",SeqListLen,"'")
                # else:
                #     print("*",SeqListLen,"*")
                # print("'",SeqListLen,"'")
                    # print('����:'+ str(self.SeqList))
                    # print('�ڶ���:' +)
                    # print('������:' + )
                    # print('������:' + )
                    # print('������:' + )
                    # print('������:' + )
            self.TraverseElementSet()

if __name__ =='__main__':
    SL=SortSequenceList()
    SL.CreateSequenceListByInput(7)
    SL.BubbleSort()
    print('�����㷨���Ϊ:')
    SL.TraverseElementSet()
