class Solution:
    def uniqueOccurrences(self,arr):
        anagram= {k:arr.count(k) for k in set(arr)}
        return True if len(set(anagram.values())) == len(anagram.values()) else False