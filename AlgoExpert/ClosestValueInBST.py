"""
:Checking the  closest value in BST
:Logic
    :Set the closest value to  -infinity
    :Compare the current node value with the target value
        :If current node value is lesser than target value then traverse the right subtree for further comparison
        :Else traverse left subtree for comparison
:Complexity:
    :Recursively
        :Average Case
            :Time - O(log(N)) where N is number of nodes in the tree
            :Space -  O(log(N)) 
                :Justification - Number of frames created for each recursive call and the memory consumption
        :Worst Case
            :Time - O(N)
                :Justification - Traversing the entire sub-tree when an element is not found
            :Space - O(N) 
    
    :Iteratively
            :Average Case
            :Time - O(log(N)) where N is number of nodes in the tree
            :Space -  O(1) 
                :Justification - No additional call is made; Only a temporary variable is being used
        :Worst Case
            :Time - O(N)
                :Justification - Traversing the entire sub-tree when an element is not found
            :Space - O(1)

"""


def findClosestValueInBSTRecursive(tree, target):
    return findClosestValueInBSTHelperRecursive(tree, target, float("-inf"))


def findClosestValueInBSTHelperRecursive(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBSTHelperRecursive(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBSTHelperRecursive(tree.right, target, closest)
    else:
        return closest


def findClosestValueInBSTIteratively(tree, target):
    return findClosestValueInBSTHelperIteratively(tree, target, float("-inf"))


def findClosestValueInBSTHelperIteratively(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - tree.value):
            closest = tree.value
        if target < tree.value:
            currentNode = currentNode.left
        elif target > tree.value:
            currentNode = currentNode.right
        else:
            break
    return closest
