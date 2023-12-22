class Solution:
    def maxScore(self,s):

        # max_score = -1
        # # Iterate the string
        # for i in range(1,len(s)):

        #     # Splitting left sub string
        #     left_s = s[:i]

        #     # Splitting right sub string
        #     right_s = s[i:]
        #     print(f"left : {left_s} and right : {right_s}")

        #     # Count no of zero in left string
        #     # zeros = left_s.count("0")
        #     zeros = 0
        #     for ch in left_s:
        #         if ch == "0":
        #             zeros += 1

        #     # Count no of ones in right string
        #     # ones = right_s.count("1")
        #     ones = 0
        #     for ch in right_s:
        #         if ch == "1":
        #             ones += 1
        #     print(f"zero : {zeros} ones : {ones}")

        #     # Calculating max score
        #     # if (zeros+ones) > max_score:
        #     #     max_score = zeros+ones
        #     t = zeros + ones
        #     if t > max_score:
        #         max_score = t
        #     print(f"max score : {max_score}")
        # return max_score

        # Initializing max score
        max_score = -1
        
        # Iterate through the string
        for i in range(1,len(s)):
            
            # Finding left sub string
            left_s = s[:i]
            
            # Finding right sub string
            right_s = s[i:]
            
            # Calculate count of zeros in left sub string
            zeros = left_s.count("0")
            
            # Calculate count of ones in right sub string
            ones = right_s.count("1")
            
            # Calculating max score
            max_score = zeros + ones if zeros+ones > max_score else max_score
        return max_score
s = Solution()
print(s.maxScore("1111"))