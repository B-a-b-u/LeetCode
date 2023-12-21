import pandas as pd
class Solution:
    def create_df(self,student_data):
        df = pd.DataFrame(student_data, columns = ["student_id","age"],copy = False,index = range(1,len(student_data)+1),dtype = ("float","float"))
        student_data[0][0] = 999999
        print(f"df : {df}")
        print(f"st : {student_data}")
        return df
    
s = Solution()
print(s.create_df([[1, 15], [2, 11], [3, 11], [4, 20]]))