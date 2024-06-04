class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Hash Map:
        Time complexity : O(n)
        Space Complexity : O(n)
        """
        freq_map = dict()   # Initialize frequency hash map

        # Populating the Freq hash map
        for ch in s:
            if freq_map.get(ch) == None:
                freq_map[ch] = 1
            else:
                freq_map[ch] += 1

        is_odd = False  # To check is there any odd frequency character
        palin_len = 0   # Calculate len of palindrom

        for v in freq_map.values():
            if v%2 == 0:    # If the freq is even add it to res
                palin_len += v
            else:
                is_odd = True
                palin_len += (v-1)  # If odd freq, add only even number len to res

        # Is even a single odd freq character is encountered, add 1 to res
        if is_odd:
            palin_len += 1
        return palin_len
    

    """
    Hash set:
    Time complexity : O(n)
    Space Complexity : O(n)
    
    seen = set()
    palin_len = 0
    for ch in s:
        if ch in seen:
            seen.remove(ch)
            palin_len += 2
        else:
            seen.add(ch)

    if len(seen) != 0:
        palin_len += 1
    return palin_len
    """