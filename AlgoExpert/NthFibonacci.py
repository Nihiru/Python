"""
:Finding the Nth fibonacci number
:Complexity
    :Recursive
        :Time
            :O(2^n)
            :Justification
                :At each level a node will have two branches at most
        :Space
            :O(N)
            :Justification  
                :N frames will be created for each function call with a given node
    
    :Memoization
        :Storing the results of recently computed function
        :Time
            :O(N)
            :Justification
                :Calculating fibonacci number from N, N-1, N-2, N-3,...0 only once 
        :Space
            : O(N)
            :Justification
                :N Frames are created for each fibonacco number
                :A hash is used to store the computed results of a function

    :Iterative
        :Store first and last numbers into an array. Compute the addition of first + last and store it then go 
         on to find the next fibonacci.
        :Time
            :O(N)
            :Justification
                :Calculating fibonacci number from N, N-1, N-2, N-3,...0 

        :Space
            :O(1)
            :Justification
                :Compute the first and last from the array and storing it as computer results
"""

# Time: O(2^N) | Space: O(N)
def getNthFibApp1(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return getNthFibApp1(n - 1) + getNthFibApp1(n - 2)


# Time:O(N)   | Space:O(N)
def getNthFibApp2(n, memoize={1: 0, 2: 1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFibApp2(n - 1, memoize) + getNthFibApp2(n - 2, memoize)
        print("Memoize", memoize)
        return memoize[n]


# Time:O(N) | Space:O(1)
def getNthFibApp3(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    # either of these conditions is specified if required fibonacci lies within the existing array
    return lastTwo[1] if n > 1 else lastTwo[0]


# print(getNthFibApp2(4))
print(getNthFibApp3(2))
