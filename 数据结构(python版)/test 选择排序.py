# coding:gbk
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


    #############################
    #�㷨8-11 ��ѡ��������㷨
    #############################
    def SimpleSelectSort(self):
        SeqListLen = len(self.SeqList)
        for i in range(1,SeqListLen-1):
            min = i
            for j in range(i+1,SeqListLen):
                if self.SeqList[min].key > self.SeqList[j].key :
                    min = j
            self.SeqList[0].key = self.SeqList[min].key
            self.SeqList[min].key = self.SeqList[i].key
            self.SeqList[i].key = self.SeqList[0].key

if __name__ =='__main__':
    SL=SortSequenceList()
    SL.CreateSequenceListByInput(6)
    SL.SimpleSelectSort()
    print('�����㷨���Ϊ:')
    SL.TraverseElementSet()
