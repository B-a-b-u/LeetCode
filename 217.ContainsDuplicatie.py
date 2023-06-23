#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Example 1:
#Input: nums = [1,2,3,1]
#Output: true
#Example 2:
#Input: nums = [1,2,3,4]
#Output: false

# Method - 1:(my version)
"""
class Solution:
    def containsDuplicate(self, nums):
        unique = set(nums)
        if len(unique) == len(nums):
            return False
        else:
            return True
"""

# Method - 2:(Brute Force => TC-O(n**2) & SC O(1)) -> time exceeds
"""
class Solution:
    def containsDuplicate(self,nums):
        for i in range(len(nums)-1):
            for j in range(len(nums))[i+1:]:
                if nums[i] == nums[j]:
                    return True
        return False

"""

# Method - 3:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for n in nums:
            if n not in hash_set:
                hash_set.add(n)
            else:
                return True
        return False

s = Solution()
print(s.containsDuplicate([2,3,4,5]))
