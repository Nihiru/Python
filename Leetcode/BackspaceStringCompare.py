# concept of MovingZeros has been implemented
def remove(source_string):
    length = 0
    for i in range(len(source_string)):
        if source_string[i] == '#':
            if length > 0:
                length-=1
        else:
            individual = list(source_string)
            individual[length] = individual[i]
            source_string = ''.join(individual)
            # str.replace(old, new, max) - replace all old substring with new substring 
            # source_string = source_string.replace(source_string[length], source_string[i]) 
            length+=1
    return length, source_string   
    
    
def backspace(S,T):
    len_s = 0
    len_t = 0
    len_s, f_s = remove(S)
    len_t, s_s = remove(T)
    if len_s != len_t: # len_s and len_t of both the strings will be based on the operation performed and not on the actual string
        return False
    else:
        for i in range(len_s):
            if f_s[i] != s_s[i]:
                return False
    return True
   
print(backspace("AB#C", "AB#C"))
print(backspace("ABC##", "AB#C#"))
print(backspace("ABCD##", "ABCD#"))
print(backspace("a##c", "#a#c"))
print(backspace("nzp#o#g","b#nzp#o#g"))