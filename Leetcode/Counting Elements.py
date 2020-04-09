def CountElements(InputList):
    """
    Count element 'x' such that 'x + 1' is also in list
    """
    count = 0
    # To have only unique elements
    # unique = set()
    # for ele  in InputList:
    #     unique.add(ele)
    
    # To allow duplicates
    for ele in InputList:
        if(ele + 1 in InputList):
            count+=1
    print(count)

CountElements([1,1,2,2])