from typing import List

# Create a hashset which is a list that doesn't 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         return len(set(nums)) != len(nums)