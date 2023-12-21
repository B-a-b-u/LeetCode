class Solution():
    def maxWidthOfVerticalArea(self,points):
        """
        This function calculates the widest vertical area between Two points
        Widest implies the x - coordinate
        So we can find the difference between two points on x coordinate which have no points in between
        First we will sort the points based on x - coordinates in Reverse order(to avoid negative sign on difference)
        Then calculate difference between two adjancent points and store those result on array
        Then return the maximum(widest) 
        """

        # Beats : 96%
        # # Sort the array based on x - coordinate in reverse order
        # points = sorted(points, key= lambda x : x[0],reverse= True)
        # res = list()
        # x1 = points[0][0]
        # for ele in points[1:]:
        #     x2 = ele[0]
        #     res.append(x1-x2)
        #     x1 = x2
        # print(f"res : {res}")
        # return max(res)

        # Beats 100%
        # Sort the array based on x - coordinate in reverse order
        points = sorted(points, key= lambda x : x[0],reverse= True)

        # Initializing widest area
        widest = -1

        # Setting x1 point as first x co-ordinate of points
        x1 = points[0][0]

        # Iterate adjacent points
        for ele in points[1:]:

            # Set x2 point
            x2 = ele[0]

            # Check if the difference is greater than widest => rewrite widest area
            if x1-x2 > widest:
                widest = x1 - x2

            # Set x1 to next element(x2) and loop set x2 to next element(x3)
            x1 = x2
        print(f"res : {widest}")
        return widest

        
s = Solution()
print(s.maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))