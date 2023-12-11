class Solution:
    def findSpecialInteger(self,arr):

        # Method 1
        # _25 = len(arr)//4
        # for ele in set(arr):
        #     count = arr.count(ele)
        #     print(f"{ele} : {count}")
        #     if count > _25:
        #         return ele
        # print(f"25% : {_25}")
        # return arr

        # Method 2 
        _25 = len(arr)//4
        print(f"25% : {_25}")
        count = {k:0 for k in set(arr)}
        print(f"count : {count}")
        for ele in arr:
            count[ele] += 1
        print(f"count : {count}")
        for k,v in count.items():
            if v > _25:
                return k
    

s = Solution()
print(s.findSpecialInteger([1,2,2,6,6,6,6,7,10]))