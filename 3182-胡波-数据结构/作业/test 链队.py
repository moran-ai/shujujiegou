# coding=gbk
class QueueNode:
    def __init__(self):
        # 初始化
        self.data = None
        self.next = None

class LinkQueue:
      # 默认初始化队列的函数
     def __init__(self):
         tQueueNode = QueueNode()  # 创建一个结点
         self.front = tQueueNode
         self.rear = tQueueNode

     # 判断队列是否为空的函数
     def IsEmptyQueue(self):
         if self.front==self.rear:
             iQueue = True
         else:
             iQueue=False
         return  iQueue

     # 入队的函数
     def EnQueue(self,data):
         # 创建新结点
         tQueueNode = QueueNode()
         tQueueNode.data = data
         # 链接到队尾
         self.rear.next = tQueueNode
         # 修改rear
         self.rear = tQueueNode
         print('当前进队的元素为:',data)

     # 出队的函数
     def DeQueue(self):
          if self.IsEmptyQueue():
              print('队列为空')
              return
          elif self.front.next.next == None:
              self.front.next = None
              self.rear =self.front
          else:
              tQueueNode = self.front.next
              self.front.next = tQueueNode.next
              return tQueueNode.data

     # 获得当前队首元素的函数



