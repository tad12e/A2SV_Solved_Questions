import sys

def solve():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = {}
    l = 0
    best_l = 0
    best_r = 0

    for r in range(n):
        freq[a[r]] = freq.get(a[r], 0) + 1

        while len(freq) > k:
            freq[a[l]] -= 1
            if freq[a[l]] == 0:
                del freq[a[l]]
            l += 1

        if r - l > best_r - best_l:
            best_l = l
            best_r = r

    print(best_l + 1, best_r + 1)

solve()