'''class Seqlist():
    def __init__(self):   # 构造函数，初始化对象
       self.SeqList = []

    # 创建顺序表
    def CreateSequenceList(self):
        print("**********")
        print('*请输入数据后回车确认，若想结束请输入#。*')
        print('**********')
        Element = input('请输入元素:')
        while Element != '#':
          self.SeqList.append(int(Element))
          Element = input('请输入元素:')

    # 删除重复元素
    def delete(self):
        print("********")
        a = int(input("请输入需要删除的元素："))
        print('')'''


a = [1,11,11,2,4,5]
print(set(a))

b = [1,2,3,4,5]
print(b[:,:,-1])