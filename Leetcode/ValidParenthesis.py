def ValidParenthesis(s):
    individualCharacters = []
    count = 0
    # Approach 1: O(N)
    # for i in paranthesisString:
    #     if i in [')','}',']']:
    #         count += 1
    #     else:
    #         individualCharacters.append(i)

    # if count == len(paranthesisString) / 2:
    #     return True

    # Approach 2: Stack
    # paranDict = {')':'(', '}':'{', ')':'('}
    # for char in paranthesisString:
    #     if char in paranDict:
    #         top_element = individualCharacters.pop() if individualCharacters else '#'
    #         if paranDict[char] != top_element:
    #             return False
    #     else:
    #         if char == "*":
    #             individualCharacters.append(')')
    #         individualCharacters.append(char)

    # return not individualCharacters  

    # Approach 3: Errichto solution (Invalid)
    # n = len(s)
    # balance = 0
    # for i in range(0,n):
    #     if s[i] == '(' or s[i] == '*':
    #         balance+=1
    #     elif balance-1 == -1:
    #         balance-=1
    #         return False
    # balance = 0
    # for i in range(n, 0, -1):
    #     if s[i] == ')' or s[i] == '*':
    #         balance+=1
    #     elif balance-1  == -1:
    #         balance-=1
    #         return False

    # Woking Solution
    leftBalance = rightBalance = 0
    n = len(s)
    for i in range(n):
            # if char is ( or * - we increment leftBalance value
        if s[i] in "(*":
           leftBalance += 1
            # else decrement it
        else:
            leftBalance -= 1
            # we check right balance value starting from the end (right side)
        if s[n-i-1] in "*)":
            rightBalance += 1
        else:
            rightBalance -= 1
            # if any balance goes negative we have the case where order of parenthesis is wrong
            # e.g. )(  -> leftBalance will be -1 and rightBalance will be -1 after first iteration
            # or ((( - leftBalance is OK, but rightBalance will be -1 after first iteration
        if leftBalance < 0  or rightBalance < 0:
            return False
    return True


print(ValidParenthesis("("))