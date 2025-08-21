    """_summary_

    Given an array of strings strs,
    group the anagrams together. 
    You can return the answer in any order.


    """

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hash_table = defaultdict(list)
        
        for i in strs:
            ''' using this iteration instead of len(strs)
            improves time complexity of your code'''
            count = [0] * 26
            
            for j in i:
                count[ord(j) - ord('a')] += 1
                
            key = tuple(count)
            hash_table[key].append(i)
                
        return list(hash_table.values())
                
            
