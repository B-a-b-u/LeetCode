class Solution:

    # My version
    def findMaxK(self, nums: list[int]) -> int:
        nums.sort() # Sort the list
        print(nums)
        i = len(nums) - 1
        j = 0
        while(j < i):
            if nums[i] < 0:
                return -1
            if nums[j] > 0:
                i -= 1
                j = 0
            if nums[j] == (-1 * nums[i]):
                return nums[i]  
            j += 1
        return -1