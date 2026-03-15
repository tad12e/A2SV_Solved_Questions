import sys
from collections import Counter

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, l, r = map(int, input().split())
    c = list(map(int, input().split()))

    L = Counter(c[:l])
    R = Counter(c[l:])

    # remove already matched pairs
    for col in list(L.keys()):
        m = min(L[col], R[col])
        L[col] -= m
        R[col] -= m
        l -= m
        r -= m


    if l > r:
        L, R = R, L
        l, r = r, l

    ans = 0
    diff = (r - l) // 2

    for col in R:
        pairs = R[col] // 2
        take = min(pairs, diff)
        ans += take
        R[col] -= take * 2
        r -= take * 2
        diff -= take

  
    ans += (r - l) // 2

   
    ans += (l + r) // 2

    print(ans)