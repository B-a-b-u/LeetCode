# With Recursion
# class Solution:
#     total_money = 0
#     on_monday = 1
#     def totalMoney(self, n: int) -> int:
#         if n <= 7:
#             self.total_money += sum(range(self.on_monday,self.on_monday+n))
#             return self.total_money
#         else:
#             self.total_money += sum(range(self.on_monday,self.on_monday+7))
#             self.on_monday += 1
#             return self.totalMoney(n-7)


# Without Recursion
class Solution:
    def totalMoney(self,n):
        total_money = 0
        on_monday = 1
        while( n > 0):
            print(f"N : {n}")
            if n <= 7 :
                total_money += sum(range(on_monday, on_monday + n))
                print(f"Total money if : {total_money}")
                return total_money
            else:
                total_money += sum(range(on_monday, on_monday + 7))
                on_monday += 1
                print(f"Total money else : {total_money}")
                n -= 7


        
s = Solution()
print(s.totalMoney(20))