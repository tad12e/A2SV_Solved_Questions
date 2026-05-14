import sys
 
 
sys.setrecursionlimit(400000)
 
def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    n = int(input[0])
    if n == 1:
        print(0)
        return
    
    adj = [[] for _ in range(n + 1)]
    idx = 1
    for _ in range(n - 1):
        u = int(input[idx])
        v = int(input[idx+1])
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
 
    
    def get_farthest(start_node):
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = [start_node]
        
        farthest_node = start_node
        max_dist = 0
        
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            
            for neighbor in adj[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)
                    if distances[neighbor] > max_dist:
                        max_dist = distances[neighbor]
                        farthest_node = neighbor
                        
        return farthest_node, max_dist
 
   
    node_u, _ = get_farthest(1)
   
    _, diameter = get_farthest(node_u)
    
    print(diameter * 3)
solve()