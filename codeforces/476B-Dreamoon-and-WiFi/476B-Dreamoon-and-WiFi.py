from math import comb

def solve():
    s1 = input()
    s2 = input()

    target = 0
    for c in s1:
        target += 1 if c == '+' else -1

    base = 0
    k = 0

    for c in s2:
        if c == '+':
            base += 1
        elif c == '-':
            base -= 1
        else:
            k += 1

    need = target - base

    # invalid case
    if (need + k) % 2 != 0:
        print(0.0)
        return

    x = (need + k) // 2

    if x < 0 or x > k:
        print(0.0)
        return

    good = comb(k, x)
    total = 2 ** k

    print(good / total)

solve()