# coding:gbk
# 算法8-1 初始化结点方法
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
        print("请输入数据：")
        for i in range(1, nElement + 1):
            a = input()
            self.SeqList.append(ListItem(int(a), i))

    def TraverseElementSet(self):
        for i in range(1, len(self.SeqList)):
            print(self.SeqList[i].key)

    #############################
    # 算法8-2 直接插入排序
    #############################
    def InsertSort(self):
        SeqListLen = len(self.SeqList)
        for i in range(0, SeqListLen):
            self.SeqList[0].key = self.SeqList[i].key
            index = i
            # print("\n第%d" % (i + 1) + "次排序为：")
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
    print('插入排序算法结果为:')
    SL.TraverseElementSet()
