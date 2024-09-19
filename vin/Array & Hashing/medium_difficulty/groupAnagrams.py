from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) 

        for word in strs:
            count = [0] * 26
                
            for letter in word:
                count[ord(letter) - ord("a")] += 1
            res[tuple(count)].append(s)

        return res.values()
    
# EXPLAINATION:
# Create a map that uses defaultdict(list) which create a map that doesn't raise errors when
# accessing keys that don't have any values. Using a temporary variable called count, keep count
# of the occurances of each alphabet and adding a 1 to that alphabet spot. Using res at the key you create "count"
# add the word as the value of that key. Return res values at the end.