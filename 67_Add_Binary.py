class Solution:

    # My solution
    def addBinary(self, a: str, b: str) -> str:
        num1 = self.binary_to_decimal(a)
        num2 = self.binary_to_decimal(b)
        print(num1,num2)
        res = num1 + num2
        res = self.decimal_to_binary(res)
        print(res)
        return res
    
    def binary_to_decimal(self,binary):
        power = 0
        dec = 0
        for i in range(len(binary)-1,-1,-1):
            if binary[i] == "1":
                dec  += 2 ** power
            power += 1
        return dec

    def decimal_to_binary(self,dec):
        if dec == 0:
            return "0"
        binary = ""
        while(dec > 0):
            binary = str(dec % 2) + binary
            dec = dec // 2
        return binary
