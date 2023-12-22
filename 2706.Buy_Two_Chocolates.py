class Solution:
    def buyChoco(self,prices,money):
        choco1,choco2 = sorted(prices)[:2]
        res = money - (choco1+choco2)
        return res if res >= 0 else money
    
s = Solution()
print(s.buyChoco([1,2,2],3))