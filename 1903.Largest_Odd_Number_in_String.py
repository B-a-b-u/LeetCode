class Solution:
    def largestOddNumber(self, num):
        # substring = [int(num[i:j]) for i in range(len(num)) for j in range(i+1,len(num)+1)]
        # print(f"Substring is  : {substring}")
        # res = [ n for n in substring if n%2 != 0]
        # print(f"result  : {res}")
        # return "" if len(res) == 0 else max(res)
        for i in range(len(num)-1,-1,-1):
            print(f"num : {num[:i+1]}")
            if(int((num[:i])[-1])%2 != 0):
                return num[:i]
        else:
            return ""


s = Solution()
print(s.largestOddNumber("34567"))
        