class Node(object):  # 创建节点类
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SingleLinkedList(object):  # 创建单链表类
        def __init__(self):
            self.head = Node(None)  # 头指针

        def CreateSingleLinked(self):  # 创建循环单链表
            Cnode = self.head
            Element = input('请输入数据:')
            while Element != '#':
                nNode = Node(int(Element))
                Cnode.next = nNode
                nNode.next = self.head
                Cnode = Cnode.next
                Element = input('请继续输入:')
        def TraverseElment(self):
            Cnode = self.head
            if Cnode.next == None:
               print('当前列表为空!')
               return
            print('当前列表为:')
            while Cnode != None:
                Cnode = Cnode.next
                self.visitElement(Cnode)

        def visitElement(self, tNode):
            if tNode != None:
                print(tNode.data, '->', end='')
            else:
                print('none')


LinkList = SingleLinkedList()
LinkList.CreateSingleLinked()
LinkList.TraverseElment()
