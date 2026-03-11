import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ops = []

    # Step 1: ensure ai < bi
    for i in range(n):
        if a[i] > b[i]:
            a[i], b[i] = b[i], a[i]
            ops.append((3, i+1))

    # Step 2: sort a
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                ops.append((1, j+1))

    # Step 3: sort b
    for i in range(n):
        for j in range(n-1):
            if b[j] > b[j+1]:
                b[j], b[j+1] = b[j+1], b[j]
                ops.append((2, j+1))

    print(len(ops))
    for op in ops:
        print(op[0], op[1])