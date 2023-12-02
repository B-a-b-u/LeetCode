
class Solution:
    #def createAnagram(self,string):
     #   anagram = {k:string.count(k) for k in set(string)}
      #  return anagram
    def groupAnagrams(self, strs):
        res = {}
        for ele in strs:
            anag = "".join(sorted(ele))
            if anag in res.keys():
                res[anag].append(ele)
                print(ele)
            else:
                res[anag] = [ele]
                print("else : ",res)
        res = list(res.values())
        return res

soln = Solution()
print(soln.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

