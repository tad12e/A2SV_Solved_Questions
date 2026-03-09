class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows=len(matrix)
        cols=len(matrix[0])
        top = 0
        bottom = rows - 1
        left = 0
        right = cols - 1
        res = []

        while top <= bottom and left <= right:
            # Traverse top row
            for i in range(left, right+1):
                res.append(matrix[top][i])
            top += 1
            
            # Traverse right column
            for i in range(top, bottom+1):
                res.append(matrix[i][right])
            right -= 1
            
            # Traverse bottom row
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
            
            # Traverse left column
            if left <= right:
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res