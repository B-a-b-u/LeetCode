class Solution:
    def finderr(self,nums):
        count_map = {k:nums.count(k) for k in range(1,len(nums)+1)}
        for k,v in count_map.items():
            if v == 2:
                err = k
            if v == 0:
                crr = k
        return [err,crr]
    
s = Solution()
print(s.finderr([1,2,2,4]))