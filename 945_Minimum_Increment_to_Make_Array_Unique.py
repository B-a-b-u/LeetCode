class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        seen = set()
        max_ele = nums[0]
        res = 0
        for n in nums:
            if n in seen:
                max_ele += 1
                seen.add(max_ele)
                res += abs(n - max_ele)
            else:
                seen.add(n)
                if n > max_ele:
                    max_ele = n
        return res