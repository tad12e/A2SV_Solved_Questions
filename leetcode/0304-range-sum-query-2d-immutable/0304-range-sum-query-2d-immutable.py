class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.matrix = []
            self.rows = 0
            self.cols = 0
            return
        
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.prefix_sum = [[0] * (self.cols + 1) for _ in range(self.rows + 1)]
        
        # Build the prefix sum matrix
        for r in range(1, self.rows + 1):
            for c in range(1, self.cols + 1):
                self.prefix_sum[r][c] = (matrix[r-1][c-1] +
                                         self.prefix_sum[r-1][c] +
                                         self.prefix_sum[r][c-1] -
                                         self.prefix_sum[r-1][c-1])

    def sumRegion(self, row1, col1, row2, col2):
        # Calculate the sum using the prefix sums
        return (self.prefix_sum[row2 + 1][col2 + 1] -
                self.prefix_sum[row1][col2 + 1] -
                self.prefix_sum[row2 + 1][col1] +
                self.prefix_sum[row1][col1])

# Example usage:
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
print(numMatrix.sumRegion(2, 1, 4, 3))  # Output: 8
print(numMatrix.sumRegion(1, 1, 2, 2))  # Output: 11
print(numMatrix.sumRegion(1, 2, 2, 4))  # Output: 12



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)