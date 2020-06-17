"""
:Logic
    :Traverse from a Node of the tree to the leaf node of a branch and then move onto the next branch
    :If the node is non-leaf node add it to the array and for leaf node apply depth-first-search
:Complexity
    :Time - O(V + E) where V is the vertices and E is the Edges that connect vertices
        :Justificatio - For traversing every node in the tree and apply DFS to nodes with non-leaf nodes
    :Space - O(V) 
        :Justification - Memory for storing visited nodes while traversing
"""


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def addChild(self, name):
        self.children.append(Node(name))

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array  # O(V) space

