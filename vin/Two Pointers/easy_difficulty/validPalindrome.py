import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.replace(" ", "")
        s1 = ""

        for i in range(len(s) - 1 , -1, -1):
            s1+=s[i]
        
        return re.sub(r'[^a-zA-Z0-9]', "", s).lower() == re.sub(r'[^a-zA-Z0-9]', "", s1).lower()

# Remove all current spaces within the sentence. Create a new string to store the flipped version.
# Store the original string into the new string in reverse order using a for loop that goes backwards.
# Return the boolean value of the only alphabetical and numerical values of both strings (removes special characters)s
