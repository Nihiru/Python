# python program to construct tree using inorder and preorder traversals

'''
:InOrder sequence
    D B E A F C
:PreOrder sequence
    A B D E C F 

:In PreOrder sequence, leftmost element is the root of the tree

:Algorithm
    :Pick an element from PreOrder and get the index as preIndex
    :Create a new tree node with data as picked element
    :Find the picked element's index in InOrder and name the index inIndex
    :Built the tree towards the left side of the inIndex as left subtree of the constructing tree
    :Built the tree towards the right side of the inIndex as right subtree of the constructing tree

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(inOrder, preOrder, inStrt, inEnd):
    if inStrt > inEnd:
        return None
   
    # pick current node from PreOrder traversal using preIndex
    # constrution of a node from PreOrder
    tNode = Node(preOrder[buildTree.preIndex])
    buildTree.preIndex += 1

    # If this node has no children then return 
    if inStrt == inEnd:
        return tNode
    
    # get the inIndex from InOrder
    inIndex = search(inOrder, inStrt, inEnd, tNode.data)

    # using index in InOrder Traversal, construct left and right subtrees
    tNode.left = buildTree(inOrder, preOrder, inStrt, inIndex-1)
    tNode.right = buildTree(inOrder, preOrder, inIndex+1, inEnd)

    return tNode
    
def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i
    
def printInOrder(node):
    if node is None:
        return
    
    printInOrder(node.left)

    print(node.data)

    printInOrder(node.right)

inOrder = ['D', 'B', 'E', 'A', 'F', 'C']
preOrder = ['A', 'B', 'D', 'E', 'C', 'F']

buildTree.preIndex = 0
root = buildTree(inOrder,preOrder, 0, len(inOrder)-1)

print("Inorder traversal of the constructe tree is : ")
printInOrder(root)

