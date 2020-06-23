"""
:Operations
    :Insert a node at a given position on a linked list, before head, after tail 
    :Delete a node from a linked list
    :Search a node in a linked list
:Logic
    :Construction of doubly linked list
:Space complexity
    :Searching
        :Time
            :O(N)
        :Space:
            :O(1)
    :Removal of a node
        :Time
            :O(1)
        :Space
            :O(1)
    :Insert at a given position:
        :Time
            :O(P) - where p is the position in the linked list
        :Space
            :O(1)        
"""


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        pass

    def setTail(self, node):
        pass

    def insertBefore(self, node, nodeToInsert):
        pass

    def insertAfter(self, node, nodeToInsert):
        pass

    def insertAtPosition(self, position, nodeToInsert):
        pass

    def removeNodesWithValue(self, value):
        pass

    def remove(self, node):
        if node == self.head:
            self.head = self.head.next

    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None
