class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        res=[]
        rows=len(image)
        cols=len(image[0])

        for i in range(rows):
            curr=[]
            for j in range(cols-1, -1,-1):
                if image[i][j]==1:
                    curr.append(0)
                else:
                    curr.append(1)
            res.append(curr)
        return res

        