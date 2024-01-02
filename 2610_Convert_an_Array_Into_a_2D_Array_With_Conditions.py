class Solution:
    def findMatrix(self,nums):
        res = list()
        t = list()
        t2 = list([1])
        # t = list(set(nums))
        # res.append(t.copy())
        while(len(t2) != 0):
            t2.clear()
            t.clear()
            for n in nums:
                if n not in t:
                    t.append(n)   
                else:
                    t2.append(n)
            nums = t2.copy()
            res.append(t.copy())  
            print(f"t : {t}, nums : {nums} res : {res}")
        
    
s = Solution()
print(s.findMatrix([1,2,3,4]))