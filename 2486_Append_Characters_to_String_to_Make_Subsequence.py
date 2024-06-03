class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        """
        Two Pointer
        Time Complexity : O(s+t)
        Space Complexity : O(1)
        """
        i = 0   # Pointer1
        j = 0   # Pointer2
        while i < len(s) and j < len(t):
            if s[i] == t[j]:    # Check if both characters are equal
                j += 1  
                i += 1
            else:
                i += 1
        
        return len(t) - j