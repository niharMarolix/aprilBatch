class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = Node(data)
        if not self.head:
            self.head = newNode

        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newNode
    
class Graph:
    def __init__(self):
        self.adjList = {}

    def addEdge(self, val1, val2):
        if val1 not in self.adjList:
            self.adjList[val1] = LinkedList()
        else:
            self.adjList[val1].append(val2)

        if val2 not in self.adjList:
            self.adjList[val2] = LinkedList()
        else:
            self.adjList[val2].append(val1)


g = Graph()
g.addEdge('vijay','raj')
g.addEdge('vijay','Vizag')
g.addEdge('vijay','Guntur')
g.addEdge('Kurnool','Vizag')
g.addEdge('Kurnool','Guntur')

for key, value in g.adjList.items():
    print(key, end = "-->")
    current = value.head
    while current:
        print(current.data, end = "-->")
        current = current.next
    print("None")