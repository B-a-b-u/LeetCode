class Solution:
    def one_minus_zeros(self,grid):
        # row = len(grid)
        # col = len(grid[0])
        # res = [[0]*col for _ in range(row)]
        # for i in range(row):
        #     for j in range(col):
        #         row_one_sum = sum(grid[i])
        #         row_zero_sum = len(grid[i]) - row_one_sum
        #         print(f"1 sum row : {row_one_sum}")
        #         print(f"0 sum row : {row_zero_sum}")
        #         column = [r[j] for r in grid]
        #         col_one_sum = sum(column)
        #         col_zero_sum = len(column) - col_one_sum
        #         print(f"1 sum col : {col_one_sum}")
        #         print(f"0 sum col : {col_zero_sum}")
        

        #         res[i][j] = row_one_sum + col_one_sum - row_zero_sum - col_zero_sum
        # return res

        row = len(grid)
        col = len(grid[0])
        res = [[0]*col for _ in range(row)]
        row_one_sum = [sum(r) for r in grid]
        col_one_sum = list()
        for c in range(col):
            col_one_sum.append(sum([r[c] for r in grid]))
        for i in range(row):
            row_zero_sum = row - row_one_sum[i]
            for j in range(col):
                col_zero_sum = col - col_one_sum[j]     
                res[i][j] = row_one_sum[i] + col_one_sum[j] - row_zero_sum - col_zero_sum
        return res
    
s = Solution()
print(s.one_minus_zeros([[0,1,1],[1,0,1],[0,0,1]]))