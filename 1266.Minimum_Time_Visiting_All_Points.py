class Solution():
    def minTimeToVisitAllPoints(self,points):
        # The Chebyshev distance
        # time = 0
        # for i,(x2,y2) in enumerate(points[1:]):
        #     x1,y1 = points[i]
        #     time += max(abs(x2-x1),abs( y2-y1))
        #     print(time)

        # return time
        time = [(max(abs(points[i+1][0]-points[i][0]),abs(points[i+1][-1]-points[i][-1]))) for i in range(len(points)-1)]
        return sum(time)

soln = Solution()
print(soln.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]]))
