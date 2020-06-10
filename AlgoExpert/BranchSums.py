"""
:To find the sum of all the leaf nodes from the root node and return them as a list
:Logic
    :
:Complexity
    :Time: O(N) 
        :Reason - Traverse N number of nodes in the tree, constant time operations(calculating the sum with current node \
                    value) for each node
    :Space: O(N)
        :Reason - affected by 
                    -List of branch sums 
                        -dictates the length of the list
                        -number of leaf nodes can not be greater than N
                        -number of leaf nodes will be N/2 roughly
                    -Recursive method implementation
                  

"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums


def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sum.append(newRunningSum)
        return
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
