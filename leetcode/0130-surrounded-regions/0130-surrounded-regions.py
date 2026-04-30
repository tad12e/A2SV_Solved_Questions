class Solution:
    def solve(self, board):
        if not board:
            return

        rows, cols = len(board), len(board[0])
        visited = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(r, c, region):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False 

            if board[r][c] == "X" or (r, c) in visited:
                return True

            visited.add((r, c))
            region.append((r, c))

            is_surrounded = True

            for dr, dc in directions:
                if not dfs(r+dr, c+dc, region):
                    is_surrounded = False

            return is_surrounded

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in visited:
                    region = []
                    if dfs(r, c, region):
                        for x, y in region:
                            board[x][y] = "X"

