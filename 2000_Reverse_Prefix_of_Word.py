"""
Given a 0-indexed string word and a character ch, reverse the segment of word that starts at index 0 and ends at the index of the first occurrence of ch (inclusive). If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string.
"""

class Solution:

    # My Initial Solution
    def reversePrefix(self, word: str, ch: str) -> str:
        word_list  = list(word)
        ch_index = -1

        # Find the index of the given character
        for i in range(len(word)):
            if word_list[i] == ch:
                ch_index = i
                break

        # If the character does not present return the word as it is
        if ch_index == -1:
            return word
        else:

            # Reverse the character from 0 to the index of the character
            i = 0
            while(i < ch_index):
                word_list[i],word_list[ch_index] = word_list[ch_index],word_list[i]
                i += 1
                ch_index -= 1
            return "".join(word_list)

        
    