class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 
class BinaryTree:
    def __init__(self):
        self.root = None

bt = BinaryTree()
bt.root=Node(1)
bt.left=Node(2)
bt.right=Node(3)
bt.left.left=Node(4)
bt.left.right=Node(5)
bt.right.left=Node(6)
bt.right.right=Node(7)

#preorder  = root left right
#postorder = left right root
#inorder = left root right