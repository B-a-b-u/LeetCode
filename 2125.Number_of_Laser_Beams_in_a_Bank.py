class Solution:
    def numberOfBeams(self,bank):
        # no_of_beams = 0
        # for i in range(len(bank)):
        #     t = 0
        #     if "1" in bank[i]:
        #         for row in bank[i+1:]:
        #             if "1" in row:
        #                 t += row.count("1")
        #                 break
        #             print(f"row : {row}")
        #     t = t * bank[i].count("1")
        #     no_of_beams += t
        # return no_of_beams

        # Optimized version
        no_of_beams = 0
        for i in range(len(bank)-1):
            if "1" in bank[i]:
                for j in range(i+1,len(bank)):
                    if "1" in bank[j]:
                        no_of_beams += bank[i].count("1") * bank[j].count("1")
                        break
            print(f"row : {bank[i]}, next : {bank[i+1]} beams : {no_of_beams}")
        return no_of_beams
    
s = Solution()
print(s.numberOfBeams(["000","111","000"]))