from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         return len(set(nums)) != len(nums)
    
# EXPLAINATION: 
# Create a hashset which is a list that only allows for unique values (no duplicates), then compare size of the two lists.