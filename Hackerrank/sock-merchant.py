# sock-merchant problem
def sockMerchant(n, arr):
    count_pairs = 0
    pairs = dict()
    
    # traverse through the entire array
    for i in range(len(arr)):
        if arr[i] in pairs.keys():
            pairs[arr[i]] = pairs.get(arr[i]) + 1
        else:
            pairs[arr[i]] = 1
    
    # count the pairs based on even numbers
    for k in pairs.keys():
        count_pairs += pairs.get(k) // 2
    return count_pairs

print(sockMerchant(7, [1,2,1,2,1,3,2]))
print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))