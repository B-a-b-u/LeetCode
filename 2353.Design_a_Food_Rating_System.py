class Solution:
    def __init__(self,foods,cuisines,ratings) -> None:
        self.menu = dict()
        for f,c,r in zip(foods, cuisines, ratings):
            if c not in self.menu.keys():
                self.menu[c] = list()
            self.menu[c].append([f,r])
            print(f"in menu : {self.menu}")

            # if not c in self.menu.keys():
            #     self.menu[c].append([f,r])
            # else:
            #     self.menu[c] = list()
            #     self.menu[c].append([f,r])
        print(f"menu : {self.menu}")

    def changeRating(self,food, newRating):
        print(f" B Menu : {self.menu}")
        for key,val in self.menu.items():
            for i,v in enumerate(val):
                if v[0] == food:
                    self.menu[key][i] = [food,newRating]
        print(f" A Menu : {self.menu}")

    def highestRating(self,cuisine):
        res = self.menu[cuisine]
        print(f"res : {res}, sort  : {sorted(res, key = lambda x : x[0])}, max : {max(res, key = lambda x : x[1])}")
        # Sorting:
        res = self.radix_sort(res)
        print(f"sort res : {res}")
        high = max(res, key = lambda x : x[1])
        print(f"hig : {high}")
        return high[0]

    def counting_sort(self, arr, exp):
        n = len(arr)
        output = [0] * n
        count = [0] * 256  # Assuming ASCII characters

        for i in range(n):
            index = ord(arr[i][0][exp]) if len(arr[i][0]) > exp else 0
            count[index] += 1

        for i in range(1, 256):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = ord(arr[i][0][exp]) if len(arr[i][0]) > exp else 0
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            arr[i] = output[i]

    def radix_sort(self, arr):
        max_length = max(len(s[0]) for s in arr)
        for i in range(max_length - 1, -1, -1):
            self.counting_sort(arr, i)
        return arr

s = Solution(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],["korean", "japanese", "japanese", "greek", "japanese", "korean"],[9, 12, 8, 15, 14, 7])
print(s.changeRating("sushi", 16))
print(s.changeRating("ramen", 16))
print(s.highestRating("japanese"))

# Initial 
"""
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_list = foods
        self.cuisine_list = cuisines
        self.rating_list = ratings 
    def changeRating(self, food: str, newRating: int) -> None:
        for i,f in enumerate(self.food_list):
            if f == food:
                self.rating_list[i] = newRating
                break
    def highestRated(self, cuisine: str) -> str:
        res = list()
        for i,c in enumerate(self.cuisine_list):
            if c == cuisine:
                res.append([self.food_list[i],self.rating_list[i]])
        high = max(sorted(res, key = lambda x : x[0]), key = lambda x : x[1])
        return high[0]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
"""