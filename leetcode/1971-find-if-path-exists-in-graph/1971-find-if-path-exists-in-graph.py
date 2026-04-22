class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        


        visited = set()
        graph = defaultdict(list)
        for a , b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node ):

            #base case
            if node == destination:
                return True
            visited.add(node)

            #path
            for nei in graph[node]:
                if nei not in visited:
                    if dfs(nei):
                        return True

            return False
        return dfs(source)