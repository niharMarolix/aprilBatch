class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None

def preorder(root):
    if root is not None:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.val)



root = Node("A")
root.left = Node("F")
root.left.left = Node("y")
root.right = Node("K")
root.right.right = Node("T")
root.left.right = Node("X")


postorder(root)