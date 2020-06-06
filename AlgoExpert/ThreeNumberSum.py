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
