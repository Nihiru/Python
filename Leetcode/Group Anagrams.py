from collections import defaultdict
def GroupAnagrams(AnagramsList):
    temp = defaultdict(list) 
    for ele in test_list: 
        temp[str(sorted(ele))].append(ele) 
    res = list(temp.values()) 


GroupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
