
#Take a look and dry run it

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

#printing root and left subtree and right subtree of a binary tree
def buildBST(arr):
    #if empty then return none
    if not arr:
        return None
        #taking 0 index of an array as a root element
    root = TreeNode(arr[0])
    #storing that root element into the stack
    stack = [root]
    #traversing to print right and left elements
    i = 1
    #traveling until the len of an array
    while i < len(arr):
        #removing that root element which was stored inside stack removed and stored into the current
        current = stack.pop(0)
        #if arr index value is not equal to -1 then append that value into current left and that value into the stack and increase the value of i same do it with the right side as well and increase i value
        if arr[i] != -1:
            current.left = TreeNode(arr[i])
            stack.append(current.left)
        i += 1
        if i < len(arr) and arr[i] != -1:
            current.right = TreeNode(arr[i])
            stack.append(current.right)
        i += 1
        #finally return root
        # The function returns the root of the constructed BST. This is because, once the construction is complete, the root is the starting point for any subsequent operations or traversals on the tree.
    return root

def findPath(root, k):
    path = []
    #if there is no elements then return empty path
    if root is None:
        return path
        #
    findPathHelper(root, k, path)
    return path

def findPathHelper(root, k, path):
    #if the root is none i.e end of the branch has been reached and function return false
    if root is None:
        return False
        #this line is crucial for tracking the path of the tree,it appends the value of the current node to the path
    path.append(root.val)
    #checks the current node has target value, k if it does the function returns true,to indicate  the path has been found
    if root.val == k:
        return True
        #this line recursively searches the target value in the left,right subtree,if found returns true
    if (root.left and findPathHelper(root.left, k, path)) or (root.right and findPathHelper(root.right, k, path)):
        return True
        #if the path value is not found in the current subtree,it backtracks by removing the lastnode(current node) from path list,to explore other posibilities
    path.pop()
    #finally if the current value is not found in the current subtree,the function returns false
    return False

# Input parsing
tree_data = list(map(int, input("enter tree elements").split()))
k = int(input("enter search elements"))

# Build BST
root = buildBST(tree_data)

# Find and print the path
result = findPath(root, k)
#if path is found it prints in a reversal manner or prints no path found
if result:
    print(" ".join(map(str, result[::-1])))
else:
    print("No path found.")
