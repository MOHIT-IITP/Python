class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
class circularLL:
    def __init__(self):
        self.head = None

    def findLastNode(self):
        current_node=self.head
        while(current_node.next!=None):
            current_node=current_node.next
        return current_node

    def insertAtbegin(self,value):
        newNode=Node(value)
        if self.head==None:
            self.head=newNode
        else:
            newNode.next=self.head
            self.head.prev=newNode
            self.head=newNode

    def insertAtend(self,value):
        newNode=Node(value)
        current_node=self.head
        if current_node==None:
            current_node=newNode
        else:
            while(current_node.next!=None):
                current_node=current_node.next
            current_node.next=newNode
            newNode.next=self.head
            self.head.prev=newNode

    def showLL(self):
        if self.head==None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
            print()

    def insertAtindex(self,value,index):
        newNode=Node(value)
        current_node=self.head
        position=0
        if current_node==None:
            current_node=newNode
        elif index==0:
            self.insertAtbegin(value)
        else:
            while(position-1!=index and current_node!=self.head):
                position+=1
                current_node=current_node.next
            newNode.next = current_node.next
            newNode.prev=current_node
            current_node.next.prev=newNode
            current_node.next=newNode
        if newNode.next==self.head:
            self.head.prev=newNode





ll=circularLL()
ll.insertAtbegin(10)
ll.insertAtbegin(90)
ll.insertAtend(20)
ll.insertAtindex(99,2)
ll.showLL()
