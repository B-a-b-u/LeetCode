class Solution:
    def evalRPN(self, tokens):
        operands = list()
        if len(tokens) == 1:
            return int(tokens[0])
        for t in tokens:
            # print(f"tok : {t}")
            if(t == "+" or t == "-" or t == "*" or t == "/"):
                # print("operator : ",t)
                y = int(operands.pop())
                x = int(operands.pop())
                res = 0
                print(f"x :{x} y : {y}")
                if t == "+":
                    res = x + y
                elif t == "-":
                    res = x - y
                elif t == "*":
                    res = x * y
                else:
                    res = int(x / y)
                # print("res : ",res)
                operands.append(res)
                # print("a res: ",operands)
            else:
                operands.append(t)
                # print("ooperand : ",operands)
            
        return operands[0]