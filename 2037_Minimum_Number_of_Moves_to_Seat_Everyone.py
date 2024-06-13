class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        """
        sorting : 
        Time Complexity : O(n logn)
        Space Complexity : O(1)
        """
        seats.sort()
        students.sort()
        min_moves = 0
        # for seat,student in zip(seats,students):
        #     min_moves += abs(seat-student)
        # return min_moves
        for i in range(len(students)):
            min_moves += abs(seats[i]-students[i])
        return min_moves
