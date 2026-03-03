import sys

def solve():
    input = sys.stdin.readline
    t = int(input().strip())

    for _ in range(t):
        n, x, k = map(int, input().split())
        s = input().strip()

        pref = [0] * (n + 1)
        for i, c in enumerate(s, 1):
            pref[i] = pref[i - 1] + (1 if c == 'R' else -1)

        # First time reaching 0 from initial position x
        first_from_x = -1
        for i in range(1, n + 1):
            if x + pref[i] == 0:
                first_from_x = i
                break

        if first_from_x == -1 or first_from_x > k:
            print(0)
            continue

        ans = 1
        remaining = k - first_from_x

        # First return to 0 when starting from 0
        cycle = -1
        for i in range(1, n + 1):
            if pref[i] == 0:
                cycle = i
                break

        if cycle != -1:
            ans += remaining // cycle

        print(ans)

if __name__ == "__main__":
    solve()