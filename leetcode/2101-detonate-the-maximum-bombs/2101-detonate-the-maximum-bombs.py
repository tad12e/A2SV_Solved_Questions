from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        ans = 0

        def dfs(i, visited):
            visited.add(i)
            x, y, r = bombs[i]
            count = 1

            for j in range(n):
                if j in visited:
                    continue

                xj, yj, _ = bombs[j]

            
                if (x - xj) ** 2 + (y - yj) ** 2 <= r ** 2:
                    count += dfs(j, visited)

            return count

        for i in range(n):
            visited = set()
            ans = max(ans, dfs(i, visited))

        return ans
                    






