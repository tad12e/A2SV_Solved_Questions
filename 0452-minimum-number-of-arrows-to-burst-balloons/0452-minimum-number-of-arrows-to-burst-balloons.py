
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:


        points.sort(key=lambda j:j[1])

        print(points)
        out=1
        end=points[0][1]


        for i in range(len(points)):
            
            if points[i][0]>end :
                print(points[i][0])
                end=points[i][1]
                #print(out)
                #print(end)
                out+=1
           
        return out
