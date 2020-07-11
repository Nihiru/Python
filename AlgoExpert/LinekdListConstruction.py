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

    # Time O(1) | Space O(1)
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # Time O(1) | Space O(1)
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # Time O(1) | Space O(1)
    # If there exists only one node
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node.prev
        nodeToInsert.next = node
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # Time O(1) | Space O(1)
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)
        nodeToInsert.prev = node
        nodeToInsert.next = node.next
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # Time: O(P) | Space:O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        node = self.head
        current_position = 1
        while node is not None and current_position != position:
            node = node.next
            current_position += 1
        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # Time: O(N) | Space: O(1)
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            # if wish to continue with traversal then following lines will makes sense
            nodeToRemove = node
            node = node.next
            if nodeToRemove.value == value:
                self.remove(nodeToRemove)

    # Time O(1) | Space O(1)
    def remove(self, node):
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        self.removeNodeBindings(node)

    """
    :Traverse the linked list and find the node with the given value exists
    """
    # Time : O(n) | Space: O(1)
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        return node is not None  # return if the node exists

    # helper methods
    def removeNodeBindings(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

