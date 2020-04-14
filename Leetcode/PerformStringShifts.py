def stringShift(s, shift):
    if not s:
        return ''
    
    for direction, by in shift:
        by = by % len(s)
        if direction == 0:
            s = s[by:] + s[:by]
        else:
            s = s[-by:] + s[:-by]
    
    return s

s = "abc"
shift = [[0,1],[1,2]]
print(stringShift(s, shift))
