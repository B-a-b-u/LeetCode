class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        """
        Time Complexity : O(n logn)
        Space complexity : O(n)
        """
        # Frequency map of arr1
        freq_map = dict()
        end_list = list()
        arr2_set = set(arr2)
        for n in arr1:
            if n not in arr2_set:
                end_list.append(n)
            if freq_map.get(n) == None:
                freq_map[n] = 1
            else:
                freq_map[n] += 1
        res = list()
        # Store relative order
        for n in arr2:
            for _ in range(freq_map[n]):
                res.append(n)
        end_list.sort()
        return res+end_list
    

"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        # Frequency map of arr1
        freq_map = dict()
        for n in arr1:
            if freq_map.get(n) == None:
                freq_map[n] = 1
            else:
                freq_map[n] += 1
        print(f"Freq map : {freq_map}")

        res = list()
        # Store relative order
        for n in arr2:
            for _ in range(freq_map[n]):
                res.append(n)
            freq_map[n] = 0
        # print(f"res : {res}")

        end_list = list()
        for k,v in freq_map.items():
            if v != 0:
                for _ in range(v):
                    end_list.append(k)
        # print(f"end list : {end_list}")
        end_list.sort()

        return res+end_list
"""