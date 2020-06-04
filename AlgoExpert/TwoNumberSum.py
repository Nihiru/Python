def TwoNumberSum(data, target):
    hash_data = dict()
    for i in data:
        if target - data in hash_data.keys():
            return (data, target - data)
        else:
            hash_data[data] = True
    return {"response": "Sum doesn't exist"}


data = [-4, -1, 1, 3, 5, 6, 8, 11]
target = 10

print(TwoNumberSum(data, target))
