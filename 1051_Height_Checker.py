class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        """
        Time Complexity : O(n logn)
        Space Complexity : O(n)
        """
        # Sort the heights and take a copy
        expected = sorted(heights)

        res = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:   # Compare 
                res += 1
        return res
    
    """
    Time Complexity = O(n+k)
    Space Complexity = O(n)
    """
    """
    # Counting sort
    count = [0] * 101

    for h in heights:
        count[h] += 1

    expected = list()
    for i in range(len(count)):
        for _ in range(count[i]):
            expected.append(i)
    print(f"Expected : {expected}")

    res = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            res += 1
    return res
    """