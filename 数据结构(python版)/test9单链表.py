class Node(object):  # 创建节点类
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class SingleLinkedList(object):    #  创建单链表类
    def __init__(self):
        self.head=Node(None)      # 头指针

    def CreateSingleLinked(self):      # 创建单链表
        Cnode = self.head
        Element = input('请输入数据:')
        while Element != '#':
           nNode = Node(int(Element))
           Cnode.next = nNode     # 头结点
           Cnode = Cnode.next     # 头结点指向下一个结点
           Element=input('请继续输入:')

    def TraverseElment(self):
        Cnode = self.head
        if Cnode.next == None:
            print('当前列表为空!')
            return
        print('当前列表为:')
        while Cnode != None:
            Cnode = Cnode.next
            self.visitElement(Cnode)

    def visitElement(self,tNode):
        if tNode != None:
            print(tNode.data,'->',end='')
        else:
            print('none')

    def InsertElementHead(self):
        Element = input('请输入新插入首端元素：')
        if Element == '#':
            return
        cNode = self.head
        nNode = Node(int(Element))
        nNode.next = cNode.next
        cNode.next = nNode

    def InsertElementTail(self):
        Element = input('请输入新插入尾端元素:')
        if Element == '#':
            return
        cNode = self.head
        nNode = Node(int(Element))
        while cNode.next != None:
            cNode = cNode.next
        cNode.next = nNode
    def DeleteElement(self):  # 删除
        Element = int(input('请输入删除的结点:'))
        cNode = self.head   # 当前
        pNode = self.head   # 之前
        if self.isEmpty():
            print('当前链表为空')
            return
        while cNode.next != None and cNode.data != Element:
            pNode = cNode
            cNode = cNode.next
        if cNode.data == Element:
            pNode.next = cNode.next
            del cNode
            print('删除成功')
        else:
            print('删除失败')

    def isEmpty(self,t):
        self.t = True


LinkList = SingleLinkedList()
LinkList.CreateSingleLinked()
LinkList.TraverseElment()
LinkList.InsertElementHead()
LinkList.TraverseElment()
LinkList.InsertElementTail()
LinkList.TraverseElment()
LinkList.DeleteElement()

