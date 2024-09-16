from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind = {}

        for i in range(len(nums)):
            dif = target - nums[i]
            
            if dif in ind.keys():
                return [ind[dif], i]

            ind[nums[i]] = i
            
        return []
    
# EXPLAINATION:
# Create a map in order to organize key value pairs of integers and their index.
# Using the difference of the target, check if the map contains the the difference and return the two indicies.
# Otherwise add the value and it's index for further use (next iterations).


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         prevMap = {}  # val -> index

#         for i, n in enumerate(nums):
#             diff = target - n
#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i
