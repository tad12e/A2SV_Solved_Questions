from collections import defaultdict

class Solution:
    def allPathsSourceTarget(self, graph):
        graphs = defaultdict(list)
        n = len(graph)

        result = []

        for i in range(len(graph)):
            for j in graph[i]:
                graphs[i].append(j)

        def dfs(node, path):
            path.append(node)

            if node == n - 1:
                result.append(path[:])  
            else:
                for i in graphs[node]:
                    dfs(i, path)

            path.pop()  

        dfs(0, [])

        return result