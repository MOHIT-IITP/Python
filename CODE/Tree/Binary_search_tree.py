class Node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

def insert(node, key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left = insert(node.left , key)
    elif key>node.key:
        node.right = insert(node.right, key)
    return node

def preorder(node):
    if node is None:
        return 
    print(node.key, end=" ")
    preorder(node.left)
    preorder(node.right)
# search method is not working rn
# def search(node,key):
#     if node is None or node.key ==key:
#         return Node(key)
#     if key<node.key:
#         return search(node.left, key)
#     else:
#         return search(node.right ,key)

Btree  = BinarySearchTree()
Btree.root = Node(10)
insert(Btree.root,2)
insert(Btree.root,23)
insert(Btree.root,4)
insert(Btree.root,72)
insert(Btree.root,98)
insert(Btree.root,11)
insert(Btree.root,20)

preorder(Btree.root)

