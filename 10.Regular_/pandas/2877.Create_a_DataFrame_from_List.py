import pandas as pd
class Solution:
    def create_df(self,student_data):
        df = pd.DataFrame(student_data, columns = ["student_id","age"])
        return df
    
s = Solution()
print(s.create_df([[1, 15], [2, 11], [3, 11], [4, 20]]))