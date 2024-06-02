class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Time complexity : O(n)
        Space Complexity : O(1)
        """
        score = 0   # To store the calculated score
        for i in range(1,len(s)):   # Iterate through 2nd character to last character
            score += abs(ord(s[i-1]) - ord(s[i]))   # Calculating absolute difference between Adjacent characters
        return score # Returning score