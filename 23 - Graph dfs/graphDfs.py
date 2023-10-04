def preorder(r,g,v):
    if r not in v: 
        v.add(r)
        print(r)

        for i in g[r]:
            newR=i
            preorder(newR,g,v)

def postorder(r,g,v):
    if r not in v:
        v.add(r)

        for i in g[r]:
            newR = i
            postorder(newR,g,v)
        print(r)


graph = {
    "A":["H","B","F","C"],
    "B":["A","D","S"],
    "C":["A","Q","E"],
    "D":["B"],
    "E":["C"],
    "F":["A","T"],
    "H":["A","I"],
    "I":["H"],
    "Q":["C"],
    "S":["B"],
    "T":["F"]    
}

root = "A"
visitedPlaces = set()
# preorder(root, graph,visitedPlaces)
postorder(root, graph,visitedPlaces)