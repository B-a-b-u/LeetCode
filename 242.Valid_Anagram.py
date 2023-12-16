class Solution:
    def anagram(self,s,t):

        # s_dict = {k:s.count(k) for k in s}
        # t_dict = {k:t.count(k) for k in t}
        # print(f"s dict : {s_dict}")
        # print(f"t dict : {t_dict}")
        # if s_dict == t_dict:
        #     return True
        # else:
        #     return False

        # s_dict = dict()
        # t_dict = dict()
        # for ch1,ch2 in zip(set(s),set(t)):
        #     print(ch1,ch2)
        #     s_dict[ch1] = s.count(ch1)
        #     t_dict[ch2] = t.count(ch2)

        # print(f"s : {s_dict}")
        # print(f"t dict : {t_dict}")

        # if s_dict == t_dict:
        #     return True
        # else:
        #     return False

        s_dict = dict()
        t_dict = dict()
        if len(s) != len(t):
            return False
        else:
            for ch1,ch2 in zip(set(s),set(t)):
                s_dict[ch1] = s.count(ch1)
                t_dict[ch2] = t.count(ch2)
            print(f"s : {s_dict}")
            print(f"t : {t_dict}")
            return True if s_dict == t_dict else False


s = Solution()
print(s.anagram("ab","bae"))
