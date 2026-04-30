        
from collections import defaultdict
class Solution:
    def getAncestors(self, n: int, edges):
        freq = defaultdict(list)

        for u, v in edges:
            freq[v].append(u)

        ans = [set() for _ in range(n)]  

        def dfs(node, visited):
            for nei in freq[node]:
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei, visited)

        for i in range(n):
            visited = set()
            dfs(i, visited)
            ans[i] = visited   

        
        return [sorted(list(s)) for s in ans]