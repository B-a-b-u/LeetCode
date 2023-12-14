class Solution:
    def special_position(self,mat):
        # no_of_sepecial_positions =  0
        # for i in range(len(mat)):
        #     for  j in range(len(mat[i])):
        #         print(f"mat : {mat[i][j]}")
        #         if mat[i][j] == 1:
        #             col = [r[j] for r in mat]
        #             row = mat[i]
        #             print(f"row : {row} col : {col} , {i}{j}")
        #             if sum(row) == 1 and sum(col) == 1:
        #                 no_of_sepecial_positions += 1
        # return no_of_sepecial_positions

        row = len(mat)
        col = len(mat[0])
        col_sum = list()
        row_sum = [sum(x) for x in mat]
        for r in range(row):
            col_sum.append(sum([x[r] for x in mat]))
        print(f"row sum : {row_sum} and col sum : {col_sum}")
        no_of_sepecial_positions =  0
        for i in range(row):
            for  j in range(col):
                print(f"mat : {mat[i][j]}")
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                        no_of_sepecial_positions += 1
        return no_of_sepecial_positions
        
    
s = Solution()
print(s.special_position([[1,0,0],[0,0,1],[1,0,0]]))