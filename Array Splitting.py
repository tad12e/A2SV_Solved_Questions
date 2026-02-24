n, k = map(int, input().split())
a = list(map(int, input().split()))

# Total cost without splitting
total_cost = a[-1] - a[0]

# If only one group
if k == 1:
    print(total_cost)
else:
    gaps = []
    
    # Compute adjacent differences
    for i in range(1, n):
        gaps.append(a[i] - a[i-1])
    
    # Sort gaps in descending order
    gaps.sort(reverse=True)
    
    # Remove largest (k-1) gaps
    reduction = sum(gaps[:k-1])
    
    print(total_cost - reduction)
