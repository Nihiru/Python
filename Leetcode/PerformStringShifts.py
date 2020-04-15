"""
shift[i] = [direction, amount]
direction can be 0 for left shift or 1 or right shit
amount is the amount by which string s to be shifted
"""
def stringShift(s, shift):
    if not s:
        return ''
    # traversal of inner lists
    for direction, by in shift:
        by = by % len(s)
        if direction == 0:
            s = s[by:] + s[:by] 
        else:
            s = s[-by:] + s[:-by]
    # Return a new string after performing an operation
    return s

s = "abc"
shift = [[0,1],[1,2]]
print(stringShift(s, shift))
