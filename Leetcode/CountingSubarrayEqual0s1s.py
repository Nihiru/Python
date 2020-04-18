def count_subarray_equals_0s_1s(ZerosOnes):
    # length of the array
    n = len(ZerosOnes)
    # creation of hash table
    um = dict()
    curr_sum = 0

    for i in range(n):
        curr_sum += (-1 if(ZerosOnes[i] == 0) else ZerosOnes[i])
        if um.get(curr_sum, None):
            um[curr_sum] += 1
        else:
            um[curr_sum] = 1

    count = 0
    # traversing of hash table
    for itr in um:
        if um[itr] > 1:
            count += ((um[itr] * int(um[itr] -1)) /2)

    # add the subarrays starting from 1st element and have equal number of 1s and 0s
    if um.get(0):
        count += um[0]
    
    return int(count)


print(count_subarray_equals_0s_1s([1,0,0,0,0,0,0]))



