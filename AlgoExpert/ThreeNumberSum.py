"""
Logic
:(x + y + z) = target
:Taking the first element as x from the list
:Traversing from x+1 till the end to find the sum of 2 numbers

Complexity
:Time Complexity = O(n^2) 
    :Justification - Implementation of 2 loops
:Space Complexity = O(1)
    :Justification - No extra space is needed
"""


def ThreeNumberSum(data, target):
    for x in range(0, len(data) - 1):
        s = set()
        curr_sum = target - data[x]
        for y in range(x + 1, len(data)):
            if (curr_sum - data[y]) in s:
                return [data[x], data[y], curr_sum - data[y]]
            s.add(data[y])
    return False


data = [-4, -1, 1, 3, 5, 6, 8, 11]
target = 20

print(ThreeNumberSum(data, target))
