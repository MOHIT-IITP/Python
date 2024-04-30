class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class doublyLL:
    def __init__(self):
        self.head=None

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
            current_node=self.head
        else:
            while(current_node.next!=None):
                current_node=current_node.next
            current_node.next=newNode
            newNode.prev=current_node
    def showLL(self):
        current_node=self.head
        while(current_node!=None):
            print(current_node.data)
            current_node=current_node.next


ll=doublyLL()
ll.insertAtbegin(10)
ll.insertAtbegin(90)
ll.insertAtend(20)
ll.showLL()


