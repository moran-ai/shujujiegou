# coding:gbk
# �㷨8-1 ��ʼ����㷽��
#######################
class ListItem(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class SortSequenceList(object):
    def __init__(self):
        self.SeqList = []

    def CreateSequenceListByInput(self, nElement):
        self.SeqList.append(ListItem(int(0), 0))
        print("���������ݣ�")
        for i in range(1, nElement + 1):
            a = input()
            self.SeqList.append(ListItem(int(a), i))

    def TraverseElementSet(self):
        for i in range(1, len(self.SeqList)):
            print(self.SeqList[i].key)

    #############################
    # �㷨8-2 ֱ�Ӳ�������
    #############################
    def InsertSort(self):
        SeqListLen = len(self.SeqList)
        for i in range(0, SeqListLen):
            self.SeqList[0].key = self.SeqList[i].key
            index = i
            # print("\n��%d" % (i + 1) + "������Ϊ��")
            # for d in range(SeqListLen):
            #     print(SeqListLen[])
            while self.SeqList[index - 1].key > self.SeqList[0].key:
                self.SeqList[index].key = self.SeqList[index - 1].key
                index = index - 1
            self.SeqList[index].key = self.SeqList[0].key

if __name__ == '__main__':
    SL = SortSequenceList()
    SL.CreateSequenceListByInput(5)
    SL.InsertSort()
    print('���������㷨���Ϊ:')
    SL.TraverseElementSet()
