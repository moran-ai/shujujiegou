# coding=gbk
class QueueNode:
    def __init__(self):
        # ��ʼ��
        self.data = None
        self.next = None

class LinkQueue:
      # Ĭ�ϳ�ʼ�����еĺ���
     def __init__(self):
         tQueueNode = QueueNode()  # ����һ�����
         self.front = tQueueNode
         self.rear = tQueueNode

     # �ж϶����Ƿ�Ϊ�յĺ���
     def IsEmptyQueue(self):
         if self.front==self.rear:
             iQueue = True
         else:
             iQueue=False
         return  iQueue

     # ��ӵĺ���
     def EnQueue(self,data):
         # �����½��
         tQueueNode = QueueNode()
         tQueueNode.data = data
         # ���ӵ���β
         self.rear.next = tQueueNode
         # �޸�rear
         self.rear = tQueueNode
         print('��ǰ���ӵ�Ԫ��Ϊ:',data)

     # ���ӵĺ���
     def DeQueue(self):
          if self.IsEmptyQueue():
              print('����Ϊ��')
              return
          elif self.front.next.next == None:
              self.front.next = None
              self.rear =self.front
          else:
              tQueueNode = self.front.next
              self.front.next = tQueueNode.next
              return tQueueNode.data

     # ��õ�ǰ����Ԫ�صĺ���



