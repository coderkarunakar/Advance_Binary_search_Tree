#check is bst or not
#Binary_Search_Tree
#search_node_in_tree
#bst2 improved solution
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None



def printTreeDetail(root):
    if root == None:
        return
    print(root.data,end=':')
    if root.left != None:
        print("L",root.left.data,end=',')
    if root.right != None:
        print('R',root.right.data,end='')
    print()
    printTreeDetail(root.left)
    printTreeDetail(root.right)



    #for better understanding please take a look inside notes as well this logic is well explained there
#taking min value and max value from the left subtree 
def minTree(root):
    #base case if the root is none then return 100000 Note:this is for left subtree
    if root == None:
        return 100000
    leftMin = minTree(root.left)
    rightMin= minTree(root.right)
    return min(leftMin,rightMin,root.data)
    #finding max value from the right subtree
def maxTree(root):
    #    #base case if the root is none then return -100000 Note:this is for right subtree
    if root == None:
        return -100000
    leftMax = maxTree(root.left)
    rightMax = maxTree(root.right)
    return max(leftMax,rightMax,root.data)
    
import queue
def TakeLevelWiseTreeInput():
    #importing the queue value
    q=queue.Queue()
    print("enter root")
    #taking the input data 
    rootData = int(input("enter root"))
    #if entered is - 1 i.e empty so return none
    if(rootData  == -1):
        return None
        #if not -1 then assigning to root value
    root = BinaryTreeNode(rootData)
    #we are adding it to the queue we use put method to append into queue
    q.put(root)
    #traversing if q is not empty
    while(not(q.empty())):
        #getting the current node value by using .get() in queue
        current_node = q.get()
        print("enter the left child of",current_node.data)
        leftchildData = int(input())
        if leftchildData!= -1:
            #assigning it to the leftchild
            leftchild = BinaryTreeNode(leftchildData)
            #assingning leftchild to current_node.left value
            current_node.left = leftchild
            #assigning leftchild to queue
            q.put(leftchild)

        print("enter the right child of ",current_node.data)
        rightchildData = int(input())
        if rightchildData!= -1:
            rightchild = BinaryTreeNode(rightchildData)
            current_node.right =rightchild
            q.put(rightchild)
    return root
    #root to node path in binary tree
#s is search element and root is the elements
def nodetoRootPath(root,s):
    #if the tree is empty return none
    if root == None:
        return None
        #if the element is found at root then simply return root
    if root.data == s:
        #creating an empty list and appending roots data and returning that list
        l = list()
        l.append(root.data)
        return l

    #now is the case the element is not at the root for sure and root is not none
    #then call it at left side
    #checking inside left subtree with the left elements and with the search value
    leftoutput = nodetoRootPath(root.left, s)
    #am able to find element at left side,if it is not none that means searching element is there and if it is none that means searching element is not there same with right subtree as well
    if leftoutput != None:
        #here using root.data since root data is also a part of the path ,and while traversing it is fetching only left subtree values not the root value so appending root value as well 
        leftoutput.append(root.data)
        return leftoutput
    rightOutput = nodetoRootPath(root.right, s)
    #am able to find  element at right side
    if rightOutput!= None:
        rightOutput.append(root.data)
        return rightOutput
        #returning none since we are not able to find it at the left,right ,and root so no where so simply returning none
    else:
        return None



root = TakeLevelWiseTreeInput()
printTreeDetail(root)
#searching path for 5 in the tree,if the element is not found simply returning None
print(nodetoRootPath(root,5))


