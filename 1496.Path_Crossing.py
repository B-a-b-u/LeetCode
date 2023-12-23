class Solution:
    def isPathCrossing(self,path):

        # Points of current position
        x,y = (0,0)

        # Store the travelled path
        travelled_path = {(x,y)}

        # Traversing specified direction
        for dir in path:
            # updating the points in respect of Direction

            if dir == "N":
                y += 1
            elif dir == "S":
                y -= 1
            elif dir == "E":
                x += 1
            elif dir == "W":
                x -= 1

            # Check current point is already travelled
            if (x,y) in travelled_path:
                return True
            
            # Otherwise add the path to travelled path
            travelled_path.add((x,y))
        return False
    
s = Solution()
print(s.isPathCrossing("NEW"))