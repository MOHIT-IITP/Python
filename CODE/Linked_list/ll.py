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
            newNode.next = newNode
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


