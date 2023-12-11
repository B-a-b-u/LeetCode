# # With numpy
# import numpy as np
# class Solution:
#     def transpose(self,matrix):
#         return np.array(matrix).T

# s = Solution()
# print(s.transpose([[1,2,3],[4,5,6]]))


# Without numpy

class Solution:
    def transpose(self,matrix):
        r = len(matrix)
        c = len(matrix[0])
        transpose = [[0]*r for _ in range(c) ]
        print(f"Tran : {transpose} , r:{r}, c:{c}")
        for row in range(len(matrix)):
            print("row :",row)
            for col in range(len(matrix[row])):
                print("col : ",col)
                transpose[col][row] = matrix[row][col]
                print(f"Matrix : {matrix[row][col]}")

        return transpose

s = Solution()
print(s.transpose([[1,2,3],[4,5,6]]))
