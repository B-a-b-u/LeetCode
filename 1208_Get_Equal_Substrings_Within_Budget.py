class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        # Brute Force
        """
        hash_map = dict()
        for ch in s+t:
            if hash_map.get(ch) == None:
                hash_map[ch] = ord(ch)
        print(f"hash map : {hash_map}")


        # Brute Force
        res = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                cost = 0
                ctrl = True
                for ch1,ch2 in zip(s[i:j+1],t[i:j+1]):
                    cost += abs(hash_map[ch1] - hash_map[ch2])
                    if cost > maxCost : 
                        ctrl = False
                        break
                if ctrl and res < j-i +1:
                        res = j-i+1

        return res
        """

        
        # Sliding Window
        # TC : O(n)
        # SC : O(1)
        start = 0   # Start of the window
        end = 0     # End of the window
        res = 0     # Maximum length of substring
        cost = 0    # Cost of current character
        while end < len(s):
            cost += abs(ord(s[end]) - ord(t[end]))  # Calculate cost of current character
            
            # If the cost is greater than max cost
            while cost > maxCost:
                cost -= abs(ord(s[start]) - ord(t[start]))  # Delete the element on left side(start)
                start += 1  # Shrink the windo in left direction
            
            # Comparing max len of substring
            if end-start+1 > res:
                res = end - start + 1

            end += 1    # Grow the window in right direction

        return res