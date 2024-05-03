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
    def insert




ll=circularLL()
ll.insertAtbegin(10)
ll.insertAtbegin(90)
ll.insertAtend(20)
ll.insertAtindex(99,2)
ll.showLL()
