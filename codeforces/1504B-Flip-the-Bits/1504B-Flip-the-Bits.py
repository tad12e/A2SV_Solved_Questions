import sys

def solve():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = input().strip()
        b = input().strip()

        balance = [False]*n
        zero = one = 0

        for i in range(n):
            if a[i] == '0':
                zero += 1
            else:
                one += 1
            if zero == one:
                balance[i] = True

        flip = 0
        possible = True

        for i in range(n-1, -1, -1):
            bit = a[i]
            if flip:
                bit = '1' if bit == '0' else '0'

            if bit == b[i]:
                continue

            if not balance[i]:
                possible = False
                break

            flip ^= 1

        print("YES" if possible else "NO")

solve()