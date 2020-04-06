def moveZeros(ListInput):
    # find the number of zeros in the list and remove them
    nxt = 0
    for x in ListInput:
       if x != 0:
          ListInput[nxt] = x
          nxt += 1 # counter to get the pointer at which to start placing 0's

    x = nxt # getting the location to insert value 0

    for i in range(len(ListInput[nxt:])):
        """
        ListInput[nxt:] : gets the element starting from 'nxt' until the last element
        len(ListInput[nxt:]) : gets the total number of elements from the 'list'
        range(len(ListInput[nxt:])) : gets the range between 0 and ListInput[nxt:]
        """

        ListInput[x] = 0 # Using the last position from where to iterate and replace all the values to 0
        x+=1 # increment to one position at a time

    print(ListInput)

moveZeros([0,1,0,22,0,2,3,0,4,5])