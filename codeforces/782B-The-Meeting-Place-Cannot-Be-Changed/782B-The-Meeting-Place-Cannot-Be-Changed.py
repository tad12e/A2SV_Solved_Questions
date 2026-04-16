import sys

def solve():
    
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    v = list(map(int, sys.stdin.readline().split()))

    def check(t):
       
        max_left = -float('inf')
        min_right = float('inf')
        
        for i in range(n):
            left = x[i] - v[i] * t
            right = x[i] + v[i] * t
            
            if left > max_left:
                max_left = left
            if right < min_right:
                min_right = right
                
        return max_left <= min_right


    low = 0.0
    high = 10**9
    for _ in range(100):
        mid = (low + high) / 2
        if check(mid):
            high = mid
        else:
            low = mid
            
    print(f"{high:.12f}")

solve()