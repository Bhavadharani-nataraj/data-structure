class Stack:
    def __init__(self):
        self.stack=[]
    def add(self,data):
        if data   not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
    def peek(self):
        return self.stack[-1]
    def print(self):
        print( self.stack)
astack=Stack()
astack.add("mon")
astack.peek()
astack.print()
