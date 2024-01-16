#Structure of BST
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self,data):
        #initially keeping root as None,and no of nodes also zero
        self.root = None
        self.numofnodes = 0
    def printTree(self):
        return
        
    def isdatapresent(self,data):
        return False
    def insert(self,data):
        return
    def deletedata(self,data):
        return False
    def count(self):
        return

b =BST()
b.insert(10) #->the 1st one will be root
b.insert(5)  #->2nd one will be roots left
b.insert(12)  # ->3rd one will be roots right
print(b.isdatapresent(10))
print(b.isdatapresent(7))
print(b.deletedata(4))
print(b.deletedata(10))
print(b.count())
b.printTree()