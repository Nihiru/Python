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
    # Approach 1: for small number of lists
    # for ele in InputList:
    #     if(ele + 1 in InputList):
    #         count+=1
    # print(count)

    # Approach 2: hashing
    # use map to count the occurences of a number in the list and add it to the map
    # InputList.sort()
    # occur_dict = {}
    # for ele in InputList:
    #     occur_dict[ele] = InputList.count(ele)

    # check element 'x + 1' exists for each element 'x'
    # for key, value in occur_dict.items():
    #     if(key +1 in InputList):
    #         count += occur_dict[key] # 6 + 9 + 7 + 6



    # Approach 3: Pro
    answer = 0 
    previous = -1
    previous_count = 0
    for x in InputList: # O(N)
        if( x == previous ): # for performing bulk operations and reduce the running time
            previous_count += 1
        else:
            if(x == previous + 1):
                answer += previous_count # finding the 'x + 1' occurences 
            previous = x 
            previous_count = 1 # Reset the count of occurrences for each number 
    print(answer)



CountElements([1,1,2,2])
CountElements([4,4,4,4,4,5,5,5,5,6,6,6,8,8,9])
CountElements([4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,7,7,7,7,7,7,8,11])