# undirected and weighted graph

class Graph:
    def __init__(self, numOfNodes):
        self.noOfNodes = numOfNodes
        self.adjMatrix = []
        for i in range(numOfNodes):
            row = [0]*numOfNodes
            self.adjMatrix.append(row)
        # print(self.adjMatrix)

    def addEdge(self,val1, val2, weight):
        self.adjMatrix[val1][val2] = weight
        self.adjMatrix[val2][val1] = weight

    def display(self):
        for i in self.adjMatrix:
            print(i)

g = Graph(4)
g.addEdge(0,1,9)
g.addEdge(0,2,5)
g.addEdge(0,3,3)
g.addEdge(2,3,8)
g.addEdge(1,3,6)
g.addEdge(1,2,4)

g.display()