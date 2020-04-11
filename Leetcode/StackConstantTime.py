"""
Stack implementation that performs push, pop, top, getMin() in constant time
"""
class MinStack:
    def __init__(self):
        # A hash where keys are lists elements and values are indexes of the list
        self.hashd = {}
        self.arr = [] 


    def push(self, element):
        """
        
        """
        if element in self.hashd:
            return
        s = len(self.arr) # get the index from 'len()'
        self.arr.append(element)
        self.hashd[element] = s # saving the index as a 'val' in this hash 

    def popElement(self, element):
        """
        Popping an item based on an element passed 
        """
        index = self.hashd.get(element, None)
        if index == None:
            return
        del self.hashd[element]

        size = len(self.arr)
        last = self.arr[size-1]

        self.arr[index], self.arr[size-1] = self.arr[size-1], self.arr[index]

        del self.arr[-1]
        self.hashd[last] = index

    def pop(self):
        """
        Pop element from the list
        """
        return self.arr.pop()

    def getMin(self):
        return min(self.arr)

    def top(self):
        """
        Returning the top most element i.e, last element from the list using negative index 
        """
        print(self.arr[-1])

    def printHash(self):
        print(self.hashd.items()) 

    def printList(self):
        for ele in self.arr:
            print(ele, sep=", ")
    
minstackObj = MinStack()
minstackObj.push(22)
# minstackObj.printHash()
minstackObj.push(33)
# minstackObj.printHash()
minstackObj.push(44)
# minstackObj.printHash()

# minstackObj.pop()
# minstackObj.printList()
# minstackObj.top()
print(minstackObj.getMin())