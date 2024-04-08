#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
#Example 1:
#Input: nums = [1,2,3,1]
#Output: true
#Example 2:
#Input: nums = [1,2,3,4]
#Output: false

class Contains_Duplicate:

    # Method1 : Solving with Brute force
    def brute_force(self,nums : list):
        """
        Searching for duplicates in a array one by one
        Time Complexity : O(n^2)
        Space Complexity : O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] == nums[j]:
                    return True
        return False
    
    # Method2 : Build-in set method
    def set_method(self,nums):
        if(len(set(nums)) == len(nums) ):
            return False
        else:
            return True
        
    # Method3 : Hash set
    

cd = Contains_Duplicate()
# print(cd.brute_force([1,1,1,3,3,4,3,2,4,2]))
# print(cd.brute_force([1,2,3,4]))

print(cd.set_method([1,1,1,3,3,4,3,2,4,2]))
print(cd.set_method([1,2,3,4]))
