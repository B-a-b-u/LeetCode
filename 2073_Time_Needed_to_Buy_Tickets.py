class Solution:

    # My Solution
    # TC : O(N^2)
    # SC : O(N)
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0    # To count total time
        while(tickets[k] != 0): # Until the target person buys the ticket
            for i in range(len(tickets)):   # Iterate through all the persons
                if tickets[i] != 0: # If anyone not got all his/her tickets
                    tickets[i] -= 1     # person buys a ticket
                    time += 1   # Time is incremented
                if tickets[k] == 0: # If target person buys a ticket then exit
                    break

            print(tickets,time)
        return time
    
    # Neetcode.io
    def neetcode(self,tickets,k):
        time = 0 # To calculate total time
        for i in range(len(tickets)) :  # Iterate through the persons
            if i <= k:
                if tickets[i] < tickets[k]:
                    time += tickets[i]
                else:
                    time += tickets[k]
            else:
                if tickets[i] < tickets[k]:
                    time  += tickets[i]
                else:
                    time += tickets[k] - 1
        return time

    

s = Solution()
print(s.neetcode([84,49,5,24,70,77,87,8],3)) #[84,49,5,24,70,77,87,8]