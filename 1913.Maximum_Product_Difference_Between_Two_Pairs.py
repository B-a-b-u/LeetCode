class Solution:
    def maxProductDifference(self,nums):
        nums = sorted(nums)
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])
    
s = Solution()
print(s.maxProductDifference([4,2,5,9,7,4,8]))