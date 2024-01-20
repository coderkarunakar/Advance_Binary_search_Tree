#Dry run it has doubt on delete data
#write code without looking and understand it
#Structure of BST
#it is used to create node and link them to construct binary tree for various application,it has data the information stored in the node,and pointers to the left and right children forming heirarchiical structure of the binary tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self,data=None):
        #initially keeping root as None,and no of nodes also zero
        self.root = None
        self.numofnodes = 0
        #just because of code readability and To make it user friendly we are using an helper function
    def printTreeHelper(self,root):
        
        #note:if you want to call recursively on left and right side then you need to pass root as your argument

        if root == None:
            return
        print(root.data,end=':')
        if root.left != None:
            print("L",root.left.data,end=',')
        if root.right != None:
            print('R',root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)

    def printTree(self):
        self.printTreeHelper(self.root)

#just returns true or false,
    def isdatapresentHelper(self,root,data):
        #if the tree is None simply return Fals
            if root ==  None:
                return False
                #if the searching data is equal to the root data then it is true,checks at every root value
            if root.data == data:
                return True
            if root.data > data:
                #call on left,and checks at every node by using above lines
                return self.isdatapresentHelper(root.left,data)
            else:
                #call on right
                return self.isdatapresentHelper(root.right,data)
        
        #THIS IS for searching the data
    def isdatapresent(self,data):
        return self.isdatapresentHelper(self.root,data)

#Note:the root remains same untill completion of the tree
    def insertHelper(self,root,data): 
        #for an empty tree we are creating an new node and returning it ,in order to insert new nodes
        #it is an empty tree, the first one will be root created
        if root == None:
            #call it a binary tree and return node and create a node with data and return this node
            node = BinaryTreeNode(data)
            return node

        #if roots data is greater than roots data then call it on left and attach it to roots left 
        if root.data > data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root
            
    def insert(self,data):

        #if it returns you the new root,then change your class root to this
        self.root=self.insertHelper(self.root, data)


    def min(self, root):
        if root == None:
            #if we want to find min of an empty set return a large no
            return 10000
            #check on left ,if left is none,root has to be min,if left is not none then simply get the min from left and return
        if root.left == None:
            return root.data
        #otherwise
        return self.min(root.left)
        #it keeps going on left,left,...and simly returns end of the left as min

    
    #creating an delete helper function,her data means what we want to delete
    def deleteDataHelper(self,root,data):
        #will return true,false, and root ,current root is none ,indicating empty tree or reaching a leaf node with out finding the data,and return false indicating data was not found and retrun a root(i.e orginal)
        if root == None:
            return False,root
        #if roots data is less than the data,call it on right side
        if root.data < data:
            #deleted (wheather data was deleted) and newrightnode (the updated right child after deletion)
            #this variable holds a boolean(if data found and deleted then True otherwise False  ,if ) value indicating wheather the deletion was successful
            #newRightNode this variable holds the updated left child of the current root after the deletion operation.it could be none if the node to be deleted was a leaf node ,or it could be a subtree after the deletion
            deleted, newRightNode = self.deleteDataHelper(root.right,data)
            #simply change right child to be the new right node,if didn't change ,keeping the same right child
            #if we delete some thing on right the overall root is not going to change,return wheather you deleted something or not and root stays the same

            #finally updates that newrightnode as rightside root and finally returns deleted(i.e True or False),root value(updated new root value)
            root.right = newRightNode
            return deleted,root
        #if root data is greater than data ,then call it on left side
        if root.data > data:
            #this line go to the next left root value and compare the data if matches then assign to newleftnode
            deleted, newLeftNode = self.deleteDataHelper(root.left,data)
            #updating the left child of the current root with the new left node returned from the recursive call
            root.left = newLeftNode
            #finally return both
            return deleted,root
             
        #special case root data == data

        #root is leaf(5 comes under this case)
        if root.left == None and root.right == None:
            return True,None
            #here return true because am deleting something and roots right becomes new root
        #root has one child roots left case
        if root.left == None:
            return True, root.right
#roots right case
        if root.right == None:
            return True,root.left
        
        #root has 2 children
        #find roots replacement by finding the min node from roots right side,then change roots data to be replacement
        replacement = self.min(root.right)
        root.data  = replacement
        deleted, newRightNode = self.deleteDataHelper(root.right, replacement)
        root.right = newRightNode
        return True,root
            



    def deletedata(self,data):
        deleted, newRoot = self.deleteDataHelper(self.root,data)
        #if actually it deleted something then we will reduce the no of nodes,and then next root is the new root and return the deleted,to tell wheather actually we deleted something or not
        if deleted:
            self.numofnodes -= 1
        self.root = newRoot
        return deleted
    def count(self):
        return self.numofnodes

b =BST()
print(b.insert(10)) #->the 1st one will be root
print(b.insert(5))  #->2nd one will be roots left
print(b.insert(12))  # ->3rd one will be roots right
print(b.insert(11))
print(b.insert(15))
print(b.printTree())
print(b.count())
print(b.deletedata(8))
print(b.printTree())
print("the tree is ",b.deletedata(5))
print(b.printTree())