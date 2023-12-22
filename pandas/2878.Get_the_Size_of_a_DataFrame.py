import pandas as pd
class Solution:
    def getDataframeSize(self,players):
        return list(players.shape)
    
s = Solution()
print(s.getDataframeSize())