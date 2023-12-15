class Solution:
    def destination(self,paths):

        # # Method 1
        # path_dict = {k:v for (k,v) in paths}
        # print(f" path dict : {path_dict}")

        # for dest in path_dict.values():
        #     print(f"is : {path_dict.get(dest)}")
        #     if path_dict.get(dest) == None:
        #         print(f"else dict : {dest}, {path_dict}")
        #         return dest

        # Optimized
        path_dict = {k:v for (k,v) in paths}
        return [dest for dest in path_dict.values() if path_dict.get(dest) == None][0]
        
s = Solution()
print(s.destination([["A","Z"]]))