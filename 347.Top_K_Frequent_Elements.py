class Solution:
    def k_frequent(self,nums,k):
    #     num_count = {k:nums.count(k) for k in set(nums)}
    #     print(f"count : {num_count}")
    #     num = [[k,v] for k,v in num_count.items()]
    #     t = sorted(num, key= lambda x : x[1])
    #     print(num)
    #     print("k : ",t)
    #     res = list()
    #     for x in t[-k:]:
    #         res.append(x[0])
    #     return res

        # Optimized
        num_count = {k:nums.count(k) for k in set(nums)}
        t = sorted(num_count.items(), key= lambda x : x[1])
        return [x[0] for x in t[-k:]]

s = Solution()
print(s.k_frequent([1,1,1,2,2,3],2))