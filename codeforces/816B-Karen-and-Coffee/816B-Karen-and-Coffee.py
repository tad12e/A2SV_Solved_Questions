def recipe():
    n, k, q = map(int, input().split())

    MAX_TEMP = 200000
    diff = [0]*(MAX_TEMP+2)

    for _ in range(n):
        l, r = map(int, input().split())
        diff[l] += 1
        diff[r+1] -= 1

    # coverage array
    cover = [0]*(MAX_TEMP+2)
    cover[0] = diff[0]

    for i in range(1, MAX_TEMP+1):
        cover[i] = cover[i-1] + diff[i]

    # good temperature array
    good = [0]*(MAX_TEMP+2)

    for i in range(MAX_TEMP+1):
        if cover[i] >= k:
            good[i] = 1

    # prefix of good
    pref = [0]*(MAX_TEMP+2)

    for i in range(1, MAX_TEMP+1):
        pref[i] = pref[i-1] + good[i]

    for _ in range(q):
        a, b = map(int, input().split())
        print(pref[b] - pref[a-1])

recipe()