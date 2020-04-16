def ValidParenthesis(paranthesisString):
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

    # Approach 2: use dictionary(mapping)
    paranDict = {')':'(', '}':'{', ')':'('}
    return False   
    print(individualCharacters)    

print(ValidParenthesis("(((((((((((()"))