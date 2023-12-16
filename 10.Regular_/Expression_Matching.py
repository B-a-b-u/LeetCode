import re
class solution:
    def match(self,s,p):
        res = re.search(p,s)
        print(f"res : {res}")
        if res:
            return True
        else:
            return False
    
s = solution()
print(s.match("aa","a*"))