class RootNode:
    def __init__(self, item):
        self.val = item
        self.right = None
        self.left = None

def lca(root, startingPoint, endPoint):
    if not root:
        return None  # Return None when the tree is empty
    
    if root.val == startingPoint or root.val == endPoint:
        return root
        
    left_lca = lca(root.left, startingPoint, endPoint)
    right_lca = lca(root.right, startingPoint, endPoint)

    if left_lca is not None and right_lca is not None:
        return root
    elif left_lca is not None:
        return left_lca
    else:
        return right_lca
    
def distance(root, node, current_distance):
    if not root:
        return float('inf')  # Return infinity when the tree is empty
    
    if root.val == node:
        return current_distance
    
    left_distance = distance(root.left, node, current_distance + 1)
    right_distance = distance(root.right, node, current_distance + 1)
    
    return min(left_distance, right_distance)

root = RootNode(1)
root.left = RootNode(2)
root.right = RootNode(3)
root.left.left = RootNode(4)
root.left.right = RootNode(5)
root.right.left = RootNode(6)
root.right.right = RootNode(7)

startingPoint = 7
endPoint = 4
lca_node = lca(root, startingPoint, endPoint)

if lca_node:
    distance_start = distance(lca_node, startingPoint, 0)
    distance_end = distance(lca_node, endPoint, 0)
    minDistance = distance_start + distance_end
    print("Lowest Common Ancestor:", lca_node.val)
    print("Minimum Distance:", minDistance)
else:
    print("One or both of the nodes not found in the tree.")
