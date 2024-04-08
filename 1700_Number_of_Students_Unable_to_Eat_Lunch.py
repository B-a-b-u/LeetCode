

class Solution:

    # My solution - Just Brute force to find the solution
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:

        # TC : O(N^3)
        # SC : O(N)

        # Iterate through the sandwiches to serve
        for sw in sandwiches.copy():
            ctrl = 0    # To preserve Infinite loop when rearranging students
            while sw != students[0]:    # Until a student willing to take that type of sandwich
                students.append(students.pop(0))    # If student not willing then move him to end of the loop
                ctrl += 1   
                if ctrl == len(students):   # The student goes to end of loop comes to first again
                    return len(students)    # Return the remaining students
            if sw == students[0]:   # If a student is willing
                sandwiches.pop(0)
                students.pop(0)        
        return len(students)
            
    # Neetcode.io
    def neetcode(self, students, sandwiches):

        # TC : O(N)
        # SC : O(N)


        res = len(students) # To calculate remaining students

        # Hashmap to store students interest
        std_count = dict()
        for s in students:
            if s in std_count:
                std_count[s] += 1
            else:
                std_count[s] = 1
        print(f"stu_count : {std_count}") 

        # Iterate through the sandwiches
        for sw in sandwiches:

            # If any students wants sandwich decrease count and no of students
            if std_count[sw] > 0:
                std_count[sw] -= 1
                res -= 1
            
            # If no one wants then return remaining students
            else:
                return res
        return res
    
    # Arjuns solution
    def arjun(self,students,sandwiches):

        # TC : O(N^3)
        # SC : O(N)

        # caluculate students length
        res = len(students)
        
        # Iterate through sandwiches
        for sw in sandwiches:
            if sw in students:
                res -= 1
                students.remove(sw)
            else:
                return res
            
        return res

s= Solution()
print(s.neetcode([1,1,1,0,0,1], [1,0,0,0,1,1]))