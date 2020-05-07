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
