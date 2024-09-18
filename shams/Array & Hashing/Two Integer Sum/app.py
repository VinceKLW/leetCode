'''

Leetcode: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Reasoning: 

First we intialize an empty dictonary. Then we iterate through the list of nums
and get the complement number that we need to find in order to add up to the target.
if the complement is in the dict we return the index of the complement and the current
index. if it is not in the dict then we keep track of where that number is and its index.


NeetCode Solution:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i


''' 


from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dict = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]

            if comp in dict:
                return [dict[comp], i]
            
            dict[nums[i]] = i
        
        return []