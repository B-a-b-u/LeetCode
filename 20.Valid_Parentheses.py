import re
class solution:
    def paranthesis(self,s):

        # # Method 1
        # open_list = list()
        # close_list = list()
        # pair = {"(" : ")", "{":"}","[":"]"}
        # valid = True

        # # Seperating open and close braces
        # for p in s:
        #     print(f"p : {p}")
        #     if p == '(' or p == '{' or p == '[':
        #         open_list.append(p)
        #     if p == ')' or p == '}' or p == ']':
        #         close_list.append(p)
        # print(f"open list : {open_list} and close list : {close_list}")

        # # Checking
        # for o in open_list.copy():
        #     print(f" o : {o}")
        #     if pair[o] in close_list:
        #         open_list.remove(o)
        #         close_list.remove(pair[o])
        
        # print(f"open list : {open_list} and close list : {close_list}")
        # if len(open_list) == 0 and len(close_list) == 0:
        #     return True
        # else:
        #     return False
        

        # # Method 2
        # symbol_list = list(s.strip())
        # print(f"Smbol list : {symbol_list}")
        # open_list = list()
        # for sym in symbol_list:
        #     if sym == '(' or sym == '{' or sym == '[':
        #         open_list.append(sym)
        #         print(f"open sym : {open_list}")
        #     if sym == ')':
        #         if '(' in open_list:
        #             open_list.remove('(')
        #             i = symbol_list.index(sym)
        #             symbol_list = symbol_list[i+1:]
        #             print(f"In ) {symbol_list}")
        #     if sym == '}' :
        #         if '{' in open_list:
        #             open_list.remove('{')
        #             i = symbol_list.index(sym)
        #             symbol_list = symbol_list[i+1:]
        #             print(f"In brace {symbol_list}")
        #     if  sym == ']':
        #         if '[' in open_list:
        #             open_list.remove('[')
        #             i = symbol_list.index(sym)
        #             symbol_list = symbol_list[i+1:]
        #             print(f"In ] {symbol_list}")

        # print(symbol_list)
        # print(open_list)

        # if len(symbol_list) == 0 and len(open_list) == 0:
        #     return True
        # else:
        #     return False
        
    
s = solution()
print(s.paranthesis("([)]"))