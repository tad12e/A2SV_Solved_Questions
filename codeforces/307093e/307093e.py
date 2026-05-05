from collections import defaultdict

n, k = map(int, input().split())
arr = list(map(int, input().split()))

freq = defaultdict(int)
l = 0
ans = 0

for r in range(n):
    freq[arr[r]] += 1

    # shrink if too many distinct elements
    while len(freq) > k:
        freq[arr[l]] -= 1
        if freq[arr[l]] == 0:
            del freq[arr[l]]
        l += 1

    # all subarrays ending at r
    ans += (r - l + 1)

print(ans)