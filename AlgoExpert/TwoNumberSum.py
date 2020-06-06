# Approach 1:
"""
Logic
:(x + y) = target => y = (target - x); where x is the number read from the list and y is the difference found in the equation
 which adds upto the target 
:Subtract the read number from the target and check whether the difference number exists in the hash
    :If yes then return the current number and the difference which adds upto target
    :Else update the hash with the number read

Complexity
:Time Complexity = O(n) 
    :Justification - Sequential accessing of the entire array
:Space Complexity = O(n)
    :Justification - extra space for the hash_table
"""


def TwoNumberSum(data, target):
    hash_data = dict()
    for x in data:
        if target - x in hash_data.keys():
            return [x, target - x]
        else:
            hash_data[x] = True
    return "Sum doesn't exist"


# Approach 2:
"""
Logic
:Sort the elements in the list and place a pointer and two extremes of the sorted list 
:Add the sum of the 2 pointers and check (list is sorted)
    :If the sum is less than target then decrement left pointer 
    :Else sum is greater than target then increment right pointer

Complexity
:Time Complexity = O(n * log(n))
    :Justification - sorting is based on quick sort
:Space Complexity = O(1)
    :Justification - extra space is not used only pointers are used to traverse the existimg list
"""


def TwoNumberSum2(data, target):
    data.sort()
    left = 0
    right = len(data) - 1
    while left < right:
        currentSum = data[left] + data[right]
        if currentSum == target:
            return [data[left], data[right]]
        elif currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
    return []


data = [-4, -1, 1, 3, 5, 6, 8, 11]
target = 10

print(TwoNumberSum2(data, target))
