'''
Binary Search Tree: A binary search tree has only 2 child nodes where data is ordered in tree format and is sorted.
Each node can have maximum of only 2 children; left should contain value less than parent node, right should contain value greater than parent node.
This hierarchy is efficient for searching, insertion and deletion.
Note: ALL VALUES MUST BE UNIQUE. CANNOT HAVE REPETITION OF VALUES.
'''
# #Structure of a node in the Binary Search tree
class Node:
    #constructor
    def __init__(self,value):
        self.left = None
        self.right = None
        self.val = value

# Operations: insertion, deletion, traversal (Pre-order, in order, post order), Searching (BSF,DFS)
# Insertion
def insert(root,val):
    #Creating the node
    temp = Node(val)
    #If there is no root, i.e tree is empty , temp becomes the root
    if root is None:
        return temp
    #Have to find the parent node for temp before inserting
    parent = None
    curnode = root
    while curnode is not None:
        parent = curnode
        if curnode.val > val:
            curnode=curnode.left
        elif curnode.val < val:
            curnode = curnode.right
        else:
            print("Value duplication.")
            return root
    #once parent is found, check if value is to be inserted to left node or right node
    if parent.val > val:
        parent.left = temp
    else:
        parent.right = temp
    return root

#Searching : Very similar to searching in a sorted array - Binary Search Algorithm



'''
Traversal - 3 types:
1. In Order : A+B
2. Pre-order : +AB
3. Post-order : AB+
Preorder and postorder is much more efficient since it uses lesser memory to compute and is faster than in order traversal.
'''
#1. In Order Traversal
def inorder(root):
    #Recursion method
    '''
    if root: #Check if root is not None
        inorder(root.left) #recursive call to inroder() for left subtree
        print(root.val, end=" - ")
        inorder(root.right) #recursive call to inroder() for right subtree
    '''

    #Iterative Method
    stack=[]
    #ans=[]
    cnode=root
    while stack or cnode:
        while cnode is not None:
            stack.append(cnode)
            cnode = cnode.left
        # current is now None, process the top of the stack
        cnode = stack.pop()
        print(cnode.val, end="-")
        # Move to the right subtree
        cnode = cnode.right




# Creating the following BST
#      50
#     /  \
#    30   70
#   / \   / \
#  20 40 60 80

r = Node(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# Print inorder traversal of the BST
inorder(r)

