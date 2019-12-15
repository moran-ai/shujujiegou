class SeqList:  # 定义顺序表类

    def __init__(self):   # 构造函数，初始化对象
       self.SeqList = []   # 创建空间


     # 创建顺序表函数

    def CreateSequenceList(self):
        print("**********")
        print('*请输入数据后回车确认，若想结束请输入#。*')
        print('**********')
        Element = input('请输入元素:')
        while Element != '#':
          self.SeqList.append(int(Element))
          Element = input('请输入元素:')

# 查找
    def FindElement(self):
        key = int(input('请输入想要查找的值:'))
        if key in self.SeqList:
            ipos = self.SeqList.index(key)
            print("查找成功！值为:", self.SeqList[ipos], "的元素，位于当前顺序表的第", ipos + 1, "个位置。")
        else:
            print('查找失败！当前顺序表中不存在值为"key"的元素')

# 插入
    def InsertElement(self):
        ipos = int(input("请输入待插入元素的位置："))
        Element = int(input("请输入待插入的值："))
        self.SeqList.insert(ipos,Element)
        print("插入元素后， 当前顺序表为：\n",self.SeqList)

# 删除
    def DeleteElement(self):
        dpos = int(input("请输入待删除的元素："))
        print("正在删除元素",self.SeqList[dpos])

        self.SeqList.remove(self.SeqList[dpos])
        print("删除后顺序表为:\n",self.SeqList)


if __name__ == '__main__':
   seqlist = SeqList ()
   seqlist.CreateSequenceList()  # 创建顺序表
   seqlist.FindElement()
   seqlist.InsertElement()
   seqlist.DeleteElement()