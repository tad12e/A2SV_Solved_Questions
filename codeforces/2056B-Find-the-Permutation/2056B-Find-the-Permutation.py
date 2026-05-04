import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    g = [input().strip() for _ in range(n)]
    
    p = [0] * (n + 1)
    
    for v in range(1, n + 1):
        # L(v) = edges to vertices with smaller value (0-indexed: 0..v-2)
        L = sum(1 for u in range(v - 1) if g[v-1][u] == '1')
        degree = g[v-1].count('1')
        pos = 1 + (n - v) + 2 * L - degree
        p[pos] = v
    
    print(*p[1:])