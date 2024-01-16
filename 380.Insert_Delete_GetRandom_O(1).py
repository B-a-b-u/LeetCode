import random
class Solution:
    def __init__(self):
        self.random_list = list()
        self.list_index = dict()

    def insert(self, val: int) -> bool:
        if val not in self.random_list:
            self.random_list.append(val)
            self.list_index[val] = len(self.random_list) - 1
            return True
        else:
            return False      

    def remove(self, val: int) -> bool:
        if val in self.random_list:
            idx = self.list_index[val]
            self.random_list[-1],self.random_list[idx] = self.random_list[idx],self.random_list[-1]
            self.list_index[self.random_list[idx]] = idx
            self.random_list.pop()
            del self.list_index[val]
            return True
        else:
            return False        

    def getRandom(self) -> int:
        return random.choice(self.random_list)