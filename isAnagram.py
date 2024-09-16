class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        if len(s) != len(t):
            return False

        for i in range (len(s)):
            if(t[i] in dict2):
                dict2[t[i]] += 1
            else:
                dict2[t[i]] = 1

            if(s[i] in dict1):
                dict1[s[i]] += 1
            else:
                dict1[s[i]] = 1

        return dict1 == dict2

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         countS, countT = {}, {}

#         for i in range(len(s)):
#             countS[s[i]] = 1 + countS.get(s[i], 0)
#             countT[t[i]] = 1 + countT.get(t[i], 0)
#         return countS == countT
