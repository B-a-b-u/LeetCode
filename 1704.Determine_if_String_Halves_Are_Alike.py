class Solution:
    def halvesAreAlike(s):

        # Version 1
        # half_len = len(s) // 2
        # first = s[:half_len]
        # last = s[half_len : ]
        # vowel_count = list((0,0))
        # for ch1,ch2 in zip(first,last):
        #     if ch1 in "aeiouAEIOU":
        #         vowel_count[0] += 1
        #     if ch2 in "aeiouAEIOU":
        #         vowel_count[1] += 1
        # if vowel_count[0] == vowel_count[1]:
        #     return True
        # else:
        #     return False

        # OPtimized
        half_len = len(s) // 2
        first = s[:half_len]
        last = s[half_len : ]
        vowel_count1,vowel_count2 = 0,0
        for ch1,ch2 in zip(first,last):
            if ch1 in "aeiouAEIOU":
                vowel_count1 += 1
            if ch2 in "aeiouAEIOU":
                vowel_count2 += 1
        if vowel_count1 == vowel_count2:
            return True
        else:
            return False

        # Version3
        # vowel_count1,vowel_count2 = 0,0
        # half_len = len(s)//2
        # for i in range(half_len):
        #     if s[i] in "aeiouAEIOU":
        #         vowel_count1 += 1
        #     if s[-(i+1)] in "aeiouAEIOU":
        #         vowel_count2 += 1
        # if vowel_count1 == vowel_count2:
        #     return True
        # else:
        #     return False
        

s = Solution()
print(s.halvesAreAlike("book"))