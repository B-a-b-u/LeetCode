"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""


# My version
"""
 Iterate through the each word characters and compare it with given character
"""
class Formed_by():
    def count_characters(self,words,chars):
        
        good_str = list()
        for w in words:
            #print("W : ",w)

            # Convert word and char into list of character
            word_list = list(w)
            char_list = list(chars)
            #print("prev w: ",word_list)
            #print("prev c: ",char_list)

            # Iterate word_list character
            for c in word_list[:]:
                print("c : ",c)
                if c in char_list:
                    print("if c : ",c)
                    word_list.remove(c)
                    char_list.remove(c)
                    print("if : ",word_list)
                    print("if : ",char_list)
                if len(word_list) == 0 :
                    good_str.append(w)

            print("Good string : ",good_str)



        return len("".join(good_str))
    

#f = Formed_by()
#print(f.count_characters(["hello","world","leetcode"],"welldonehoneyr"))


# Chatgpt optimization of my code
# Check through character count
class Formed_by_gpt():
    def count_characters(self,words,chars):
        good_str_len = 0
        char_anag = { c:chars.count(c) for c in chars}
        print(char_anag)

        for word in words:
            word_anag = { w:word.count(w) for w in word}
            
            valid = True
            for w,count in word_anag.items():
                try:
                    if(char_anag[w] < count):
                        valid = False
                        break
                except KeyError:
                    break
            if valid:
                good_str_len += len(word)

        return good_str_len

f2 = Formed_by_gpt()
print(f2.count_characters(["hello","world","leetcode"],"welldonehoneyr"))