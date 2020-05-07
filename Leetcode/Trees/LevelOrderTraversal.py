class Node:
    def __init__(self, key):
        self.value = key
        self.right = None
        self.left = None

'''
:Nodes at a given level 
'''
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.value)
    else:
        printGivenLevel(root.left, level-1)
        printGivenLevel(root.right, level-1)


'''
:Height of a tree
    :The number of nodes along the longest path from the root node down to the farthest leaf node
'''
def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        # to identify the highest weight of a sub-tree at a given level
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


root = Node(100)
