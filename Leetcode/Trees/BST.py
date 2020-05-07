'''
Binary Search Tree in action
'''
class Node:
    # what a node supposed to have 
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# an insert operation that specifies 
def insert(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            # condition to check if the right node is empty
            if root.right is None:
                root.right = node
            # pass right node as root
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

#  Increasing order
def inorderTraversalIncreasing(root):
    if root:
        inorderTraversalIncreasing(root.left)
        print(root.val)
        inorderTraversalIncreasing(root.right)


# Decreasing order
def inorderTraversalDecreasing(root):
    if root:
        inorderTraversalDecreasing(root.right)
        print(root.val)
        inorderTraversalDecreasing(root.left)


def postorderTraversal(root):
    if root:
        postorderTraversal(root.left)
        postorderTraversal(root.right)
        print(root.val)


def preorderTraversal(root):
    if root:
        print(root.val)
        preorderTraversal(root.left)
        preorderTraversal(root.right)

r = Node(50)
insert(r, Node(30))
insert(r, Node(20))
insert(r, Node(40))
insert(r, Node(70))
insert(r, Node(60))
insert(r, Node(80))

# inorderTraversalIncreasing(r)
inorderTraversalDecreasing(r)
# postorderTraversal(r)
# preorderTraversal(r)