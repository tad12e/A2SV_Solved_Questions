import sys

def solve():
    # Use fast I/O for large inputs
    input = sys.stdin.read().split()
    t = int(input[0])
    idx = 1
    
    results = []
    for _ in range(t):
        n = int(input[idx])
        s = input[idx+1]
        idx += 2
        
        ans = -1
        
        # Check all possible small valid substrings
        if "aa" in s:
            ans = 2
        elif "aba" in s or "aca" in s:
            ans = 3
        elif "abca" in s or "acba" in s:
            ans = 4
        elif "abbacca" in s or "accabba" in s:
            ans = 7
        else:
            ans = -1
            
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()
