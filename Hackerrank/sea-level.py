'''
:valley 
    :its below sea level
:mountain:
    :its above sea level
'''
def countingValley(n, s):
    sl = list(s)
    valley_count = 0
    level = 0
    for i in sl:
        if i == 'U':
            valley_count += 1
        elif i == 'D':
            valley_count -= 1
            # number of times 'x' has traversed through the valley
            if valley_count == -1:
                level += 1
    return level

print(countingValley(8, 'UDDDUDUU'))
