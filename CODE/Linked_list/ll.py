class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
    self.head = None

    def insertAtend(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            currentNode = self.head
            while(currentNode.next!=None):
                currentNode=currentNode.next
            currentNode.next = newNode
    def insertAtbegin(self,value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head 
            self.head = newNode

    def insertAtindex(self,value,index):
        newNode = Node(value)
        position=0
        currentNode = self.head
        if position == index:
            self.insertAtbegin(value)
        else:
            while(currentNode!=None and position+1!=index):
                position+=1
                currentNode=currentNode.next
            if currentNode != None:
                newNode.next = currentNode.next
                currentNode.next = newNode
            else:
                print("Index is not present")
    def updateAnode(self,value,index):
        newNode = Node(value)
        current_position=0
        temp=self.head
        if temp==None:
            temp=newNode
        else:
            while(current_position!=index-1):
                current_position+=1
                temp=temp.next
            if temp!=None:
                newNode.next=temp.next.next
                temp.next=newNode
            else:
                print("index is not present")


