import sys
from collections import Counter

def solve():
    input = sys.stdin.read().split()
    if not input:
        return
    
    T_cases = int(input[0])
    ptr = 1
    
    results = []
    for _ in range(T_cases):
        s = input[ptr]
        t = input[ptr+1]
        ptr += 2
        
        count_s = Counter(s)
        count_t = Counter(t)
        
        # 1. Feasibility check
        possible = True
        for char, count in count_s.items():
            if count_t[char] < count:
                possible = False
                break
        
        if not possible:
            results.append("Impossible")
            continue
            
        # 2. Identify leftover characters
        leftovers = []
        # Subtract s from t
        temp_t = count_t.copy()
        for char in s:
            temp_t[char] -= 1
            
        for char in sorted(temp_t.keys()):
            leftovers.extend([char] * temp_t[char])
            
        # 3. Greedy Merge
        res = []
        left_ptr = 0
        s_ptr = 0
        
        while s_ptr < len(s) and left_ptr < len(leftovers):
            # If the leftover char is smaller, take it to keep string lexicographically small
            if leftovers[left_ptr] < s[s_ptr]:
                res.append(leftovers[left_ptr])
                left_ptr += 1
            else:
                # If s[s_ptr] is smaller or equal, we MUST place it now to 
                # keep s as a subsequence and maintain order.
                res.append(s[s_ptr])
                s_ptr += 1
        
        # 4. Add remaining characters
        res.extend(s[s_ptr:])
        res.extend(leftovers[left_ptr:])
        
        results.append("".join(res))

    print("\n".join(results))

if __name__ == "__main__":
    solve()