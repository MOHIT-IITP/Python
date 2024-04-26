class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
    self.head = None

    def insertAtbegin(self,value):
        newNode = Node(value)

