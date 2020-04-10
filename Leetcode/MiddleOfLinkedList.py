class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

    def printLinkedList(self):
        temp = self
        while(temp.next != None):
            print(temp.data, sep="\n")
            temp = temp.next

def MiddleElement(NodeList):
    """
    Implemented tortoise and Hare problem

    """
    A = NodeList
    B = NodeList
    middle = []
    while(B != None):
        B = B.next
        if(B == None):
            return A
        A = A.next
        B = B.next
    return A
   

def CreateLinkedList(NodeList):
    """
    Creation of a linked list from a sequence of data
    """
    LinkedListObj = None
    for ele in NodeList:
        newObj = Node(ele)
        # only for first element in the sequence
        if not isinstance(LinkedListObj, Node):
            LinkedListObj = newObj
        else:
            temp = LinkedListObj
            while(temp.next != None):
                temp = temp.next
            temp.next = newObj  

    print(MiddleElement(LinkedListObj))

CreateLinkedList([1,2,3,4,5,6,7])
