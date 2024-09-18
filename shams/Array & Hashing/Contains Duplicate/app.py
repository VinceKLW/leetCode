'''

Leetcode: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Solution: 

Perform a hashset function on the list to get rid of duplicates and compare
sizes of the array before and after performing this operation. If the length differs
then we know there is a duplicate that was removed

'''



from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         return len(set(nums)) != len(nums)
    
solution = Solution()

print(solution.hasDuplicate([1, 2, 3, 3])) # true
print(solution.hasDuplicate([1, 2, 3, 4])) # false
