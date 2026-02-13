class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        out=0

        row=len(grid)
        cols=len(grid[0])
        for i in range(row):
            for j in range(cols):
                if  grid[i][j]<0:
                    out+=cols-j
                    break

        return out

        