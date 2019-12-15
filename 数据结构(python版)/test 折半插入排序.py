# coding:gbk
#################################################################
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
    # �㷨8-3 �۰��������
    #############################
    def BinInsertSort(self):
        SeqListLen = len(self.SeqList)
        for i in range(2, SeqListLen):
            SeqLeft = 1
            SeqRight = i - 1
            self.SeqList[0].key = self.SeqList[i].key
            while SeqLeft <= SeqRight:
                SeqMid = (SeqLeft + SeqRight) // 2
                if self.SeqList[SeqMid].key > self.SeqList[0].key:
                    SeqRight = SeqMid - 1
                    # print(SeqRight)
                else:
                    SeqLeft = SeqMid + 1
                    # print(SeqRight)
            j = i - 1
            while j >= SeqLeft:
                self.SeqList[j + 1].key = self.SeqList[j].key
                j = j - 1
                # print(j)
            self.SeqList[SeqLeft].key = self.SeqList[0].key

if __name__ == '__main__':
    SL = SortSequenceList()
    SL.CreateSequenceListByInput(5)
    SL.BinInsertSort()
    print('�۰���������㷨���Ϊ:')
    SL.TraverseElementSet()
