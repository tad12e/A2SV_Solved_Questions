class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        cols, rows=len(boxGrid), len(boxGrid[0])
        ans=[]
        for i in range(cols):
            for j in range(rows-1, -1, -1):
                if boxGrid[i][j] == ".":
                    k = j - 1
                    while k >= 0 and boxGrid[i][k] == ".":
                        k -= 1
                    if k >= 0 and boxGrid[i][k] == "#":
                        boxGrid[i][j], boxGrid[i][k] = boxGrid[i][k], boxGrid[i][j]
            
        print(boxGrid)
        for i in range(rows):
            curr=[]
            for j in range(cols-1, -1, -1):
                curr.append(boxGrid[j][i])
            ans.append(curr)
        return ans

                
        




        