class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 
class BinaryTree:
    def __init__(self):
        self.root = None
# creating a inorder traversal in binary tree
def Inorder(node):
    if node is None:
        return
    Inorder(node.left)
    print(node.data, end=" ")
    Inorder(node.right)

# creating a preorder traversal in binary tree
def preorder(node):
    if node is None:
        return
    print(node.data, end=" ")
    preorder(node.left)
    preorder(node.right)

# creating a postorder traversal in binary tree
def postorder(node):
    if node is None:
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.data, end=" ")

bt = BinaryTree()
bt.root=Node(1)
bt.root.left=Node(2)
bt.root.right=Node(3)
bt.root.left.right=Node(5)
bt.root.left.left=Node(4)
bt.root.right.left=Node(6)
bt.root.right.right=Node(7)


# printing the preorder 
print("preorder: ")
preorder(bt.root)
print("\n")

# printing the inorder
print("inorder : ")
Inorder(bt.root)
print("\n")

# printing the postorder
print("postorder : ")
postorder(bt.root)
# main thing to keep in mind: 
#preorder  = root left right
#postorder = left right root
#inorder = left root right
