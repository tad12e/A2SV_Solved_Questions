class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        cols=len(matrix)
        row=len(matrix[0])


        res=[]

        for i in range(row):
            new_row=[]
            for j in range(cols):
                new_row.append(matrix[j][i])
            res.append(new_row)
        return res
        