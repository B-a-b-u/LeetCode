class Solution:
    def largestGoodInteger(self, num: str) -> str:
        good = list()
        for i in range(len(num)-2):
            if(num[i] == num[i+1] == num[i+2] and num[i]*3 not in good):
                good.append(num[i]*3)
        if len(good) == 0:
            return ""
        else:
            return max(good)
    