from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = sorted(set(nums))

        count = 1
        largest_count = 1

        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            else:
                largest_count = max(largest_count, count)
                count = 1
        
        largest_count = max(largest_count, count) 

        return largest_count
