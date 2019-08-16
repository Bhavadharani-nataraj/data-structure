class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def printtree(self):
        print(self.data)
root=Node(10)
root=Node(20)
root.printtree()
