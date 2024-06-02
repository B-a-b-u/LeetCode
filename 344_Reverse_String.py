class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Two Pointers
        Time Complexity : O(n)
        Space Complexity : O(1)
        """
        i = 0       # pointer1 : starting position
        j = len(s) - 1  # pointer2 : last position
        while(i < j):   # Iterate until i and j crosses or equal
            s[i],s[j] = s[j],s[i]   # Use tuple assignment for swapping in single line
            i += 1  # increment pointer
            j -= 1  # decrement pointer