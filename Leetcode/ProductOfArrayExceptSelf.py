def productExceptSelf(nums):
    """
    Return an array 'output' such that output[i] is equal to the product of all the elements of nums except nums[i]
    """
    # Approach 1: Time and space complexity is O(N) 
    # length = len(nums)
        
   
    # L, R, answer = [0]*length, [0]*length, [0]*length
        
    # L[0] = 1
    # for i in range(1, length):
    #     L[i] = nums[i - 1] * L[i - 1]
       
    # for i in reversed(range(length - 1)):
    #     R[i] = nums[i + 1] * R[i + 1]
        
    #     # Constructing the answer array
    # for i in range(length):
    #     answer[i] = L[i] * R[i]
        

    # Aprroach 2: 
    length = len(nums)
    answer = [0] * length
    answer[0] = 1
    for i in range(1, len(nums)):
        answer[i] = answer[i-1] * nums[i-1]

    R = 1
    for i in reversed(range(length)):
        answer[i] = answer[i]  * R
        R *= nums[i]
        
    return answer

print(productExceptSelf([4,5,1,8]))
