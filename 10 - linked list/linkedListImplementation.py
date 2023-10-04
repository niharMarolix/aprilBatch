'''
Delete : Deletes an element using the given key.
'''

class LinkedList:

    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def append(self, data):
        newNode = self.Node(data)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def insertionAtBegining(self,data):
        newNode = self.Node(data)
        newNode.next = self.head
        self.head = newNode

    def dAB(self): # deletion at begining
        if self.head:
            self.head = self.head.next
        else:
            return("linked list is empty")

    def displayLL(self):
        current = self.head
        while current:
            print(current.data, end = "-->")
            current = current.next
        print("None")

    def searching(self, key):
        index = 0
        temp = self.head
        while temp:
            if temp.data ==key:
                return index
            temp = temp.next
            index = index+1
        return("key not found")
    
    def deletingByKey(self,key):
        current = self.head

        if current and current.data ==key:
            self.head = current.next
            current = None
            return
        
        previous = None
        while current and current.data !=key:
            previous = current
            current = current.next

        if current is None:
            return
        
        previous.next = current.next
        current = None



l = LinkedList()
l.append("USA")
l.append("India")
l.append("Nepal")
l.append("UK")
l.insertionAtBegining("Kothaguda")
# print(l.dAB())

print(l.searching("Nepal"))
l.displayLL()


# l.displayLL()