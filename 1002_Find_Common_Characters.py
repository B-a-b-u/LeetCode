class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        
        # Anagram for first element
        anag = dict()
        for ch in words[0]:
            if anag.get(ch) == None:
                anag[ch] = 1
            else:
                anag[ch] += 1
        print(f"anag : {anag}")
        for word in words[1:]:
            temp_anag = dict()
            for ch in word:
                if temp_anag.get(ch) == None:
                    temp_anag[ch] = 1
                else:
                    temp_anag[ch] += 1
            print(f"temp : {temp_anag}")

            for k,v in anag.copy().items():
                if temp_anag.get(k) == None:
                    anag.pop(k)
                else:
                    anag[k] = min(temp_anag[k],v)
        print(f"Last anag : {anag}")

        res = ""
        for k,v in anag.items():
            res += (k * v)

        return list(res)

        """
        Improvised

        class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # Anagram for first element
        anag = dict()
        for ch in words[0]:
            if anag.get(ch) == None:
                anag[ch] = 1
            else:
                anag[ch] += 1
        print(f"anag : {anag}")
        for word in words[1:]:
            temp_anag = dict()
            for ch in word:
                if temp_anag.get(ch) == None:
                    temp_anag[ch] = 1
                else:
                    temp_anag[ch] += 1
            print(f"temp : {temp_anag}")

            for k in anag:
                anag[k] = min(anag[k], temp_anag.get(k,0))
        print(f"Last anag : {anag}")

        res = list()
        for k,v in anag.items():
            for _ in range(v):
                res.append(k)
        return list(res)
        """