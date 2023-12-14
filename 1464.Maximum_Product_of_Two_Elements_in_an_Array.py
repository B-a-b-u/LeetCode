class solution:
    def maxProduct(self,nums):

        # Method 1
        # high1 = max(nums)
        # nums.remove(high1)
        # print(f"High 1 : {high1}, {nums}")
        # high2 = max(nums)
        # print(f"High2 : {high2}")

        # Method 2
        high1 = 0
        high2 = 0
        for n in nums:
            print(f"N : {n}")
            if n >= high1:
                high2 = high1
                print(f"High 2 : {high2}")
                high1 = n
                print(f"High 1 : {high1}")
            else:
                high2 = max(high2,n)
        return (high1-1)*(high2-1)

        # Method 3
        # nums.sort()
        # return (nums[-1]-1)*(nums[-2]-1)

        # # Method 4
        # max = 0
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
        #         t = (nums[i]-1)*(nums[j]-1)
        #         if t > max:
        #             max = t
        # return max

s = solution()
print(s.maxProduct([10,2,5,2]))