class Solution:
    def maxLengthBetweenEqualCharacters(self,s):
        # res = -1
        # for i in range(len(s)):
        #     max_len = 0
        #     if s[i] in s[i+1:]:
        #         for j in range(len(s[::-1])):
        #             j = len(s) - j -1
        #             if s[i] == s[j]:
        #                 print("ch : ",s[i+1:j+1],len(s[i+1:j+1]))
        #                 max_len = len(s[i+1:j])
        #             print(f"res : {res}, len : {max_len}")
        #             if max_len > res:
        #                 res = max_len
        #                 print(f"res: {res}")
        # return res

        # Optimized version
        char_index = dict()
        max_len = 0
        if len(s) == len(set(s)):
            return -1
        for i,ch in enumerate(s):
            if ch not in char_index:
                char_index[ch] = i
            else:
                print(f"i : {i}, already : {char_index[ch]}, {i - char_index[ch] - 1}")
                if max_len < i - char_index[ch] - 1:
                    max_len = i - char_index[ch] - 1
            print("char index ",char_index)
s = Solution()
print(s.maxLengthBetweenEqualCharacters("abar"))