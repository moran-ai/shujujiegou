class SenuenceQueue:
    # 默认初始化队列的函数
    def __init__(self):
        self.MaxQueueSize = 4
        self.s = [None for x in range(0,self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    # 判断队列为空的函数
    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    # 元素入队的函数
    def EnQueue(self,x):
        if (self.rear < self.MaxQueueSize -1):
            self.rear = self.rear+1
            self.s[self.rear] = x
            print('当前进队元素为:', x)
        else:
            print('队列已满，无法入队')
            return

    # 元素出队的函数
    def DqQueue(self):
        if self.IsEmptyQueue():
            print('队列为空，无法出队')
            return
        else:
            self.front = self.front+1
            return self.s[self.front]

    # 获取当前队首元素的函数
    def GetHead(self):
        if self.IsEmptyQueue():
            print('队列为空，无法输出队首元素')
            return
        else:
            return self.s[self.front + 1]

    # 依次访问队列中元素的函数
    def QueueTraverse(self):
        if self.IsEmptyQueue():
            print('队列为空')
            return
        else:
            for i in range(self.front,self.rear):
                print(self.s[i+1], end=' ')

    # 由用户输入元素将其进队的函数
    def GreatQueueByInput(self):
        data = input('请输入元素(继续输入请按回车，结束输入请按''#：')
        while data != '#':
            self.EnQueue(data)
            data = input('请输入元素:')
    # 获取队列长度
    def length(self):
        return (self.rear-self.front+self.MaxQueueSize)%self.MaxQueueSize

# 主程序
sq = SenuenceQueue()
sq.GreatQueueByInput()
print('队内的元素为：',end=' ')
sq.QueueTraverse()
print('队首元素为:')
print(sq.GetHead())
print('队列长度为：',(sq.length()))
