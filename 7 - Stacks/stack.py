class NewStack:
    def __init__(self, stack):
        self.stack = []


    def checkIfEmpty(self,stack):
        return len(self.stack)==0

    def checkIfFull(self,stack):
        return len(self.stack) == 5

    def pushOps(self,stack, element):
        s = (self.checkIfFull(stack))
        if s is True:
            print("Stack is full use pop method first to add element")
            return("Stack is full use pop method first to add element")
        else:
            self.stack.append(element)

    def poppingFromTheTop(self,stack):
        s = (self.checkIfEmpty(stack))
        if s is True:
            return("Stack is empty add some elemets")
        else:
            stack.pop()

    def peek(self,stack):
        return("top value is : ",s.stack[-1])

s = NewStack([])
(s.poppingFromTheTop(s.stack))
(s.pushOps(s.stack,1))
(s.peek(s.stack))
(s.pushOps(s.stack,4))
(s.pushOps(s.stack,5))
(s.pushOps(s.stack,6))
(s.poppingFromTheTop(s.stack))
(s.poppingFromTheTop(s.stack))
(s.pushOps(s.stack,7))
(s.pushOps(s.stack,0))
(s.pushOps(s.stack,4))
(s.pushOps(s.stack,2))
(s.pushOps(s.stack,3))
(s.pushOps(s.stack,90))
print(s.stack)

