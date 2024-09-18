'''

Leetcode: Easy
Time Complexity: O(n)
Space Complexity: O(n)

Reasoning: 

First, we compare the lengths of the two words. If they differ, the words can't be anagrams. 
If the lengths match, we initialize dictionaries for both words and iterate through their characters. 
Using `.get`, we retrieve the current letter count in the dictionary, then update it. Once all letters 
are processed, we compare the two dictionaries to check if both the letters and their counts match.

NeetCode Solution:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDict, tDict = {}, {}

        for i in range(len(s)):
            sDict[s[i]] = 1 + sDict.get(s[i], 0)
            tDict[t[i]] = 1 + tDict.get(t[i], 0)

        return sDict == tDict
        


solution = Solution()
print(solution.isAnagram("racecar", "carrace"))

