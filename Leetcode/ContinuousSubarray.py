def findMaxLength(nums):
    counts = {0:-1}
    max_len = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count  += -1
        else:
            count +=  1

        if count in counts:
            max_len = max(max_len, i- counts.get(count))
        else:
            counts[count] = i
    return max_len 


print(findMaxLength([0,1]))