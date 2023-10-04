class RootNode:
    def __init__(self, item):
        self.val = item
        self.right = None
        self.left = None

def bfs(root):
    if not root:
        return("tree is empty")
    else:

        queu = []
        queu.append(root)

        while queu:
            node = queu.pop(0)
            print(node.val)

            if node.left:
                queu.append(node.left)

            if node.right:
                queu.append(node.right)

root = RootNode(1)
root.left = RootNode(2)
root.right = RootNode(3)
root.right.left = RootNode(6)
root.left.left = RootNode(4)
root.left.right = RootNode(5)

bfs(root)