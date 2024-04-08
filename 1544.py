s = "abBAcC"

i = 0
while(i < len(s)-1):

    if(s[i].isupper() and s[i+1].islower() and s[i].casefold() == s[i+1].casefold()):
        print(i,i+1)
        s = list(s)
        s[i] = ""
        s[i+1] = ""
        s = "".join(s)
        print("r1",s)
    elif(s[i+1].isupper() and s[i].islower() and s[i].casefold() == s[i+1].casefold()):
        print(i,i+1)
        s = list(s)
        s[i] = ""
        s[i+1] = ""
        s = "".join(s)
        print("r",s)
    i+=1



print(s)
