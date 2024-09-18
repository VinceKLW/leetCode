from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        values = {}
        result = []

        for i in range (len(nums)):
            if nums[i] in values:
                values[nums[i]]+=1
            else:
                values[nums[i]] = 1

        sorted_dict = sorted(values.items(), key=lambda x: x[1], reverse=True)

        for i in range(k):
            result.append(sorted_dict[i][0])

        return result

