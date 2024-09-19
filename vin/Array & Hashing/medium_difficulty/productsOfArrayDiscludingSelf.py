from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums1 = []

        for i in range(len(nums)):
            nums1.append(1)
            for j in range(len(nums)):
                if(j!=i):
                    nums1[i] *= nums[j]
        return nums1
    
# Create an array that will hold the new values which will be adjusted in the for loops. 
# First for loop will add a value of 1 to the index, the second for loop will only multiply
# the index by the original array index if the index it not itself (j!=i).
# Return new array.