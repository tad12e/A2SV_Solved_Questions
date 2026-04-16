def nextLvl():
   
    parts = input().split()
    if len(parts) == 2:
        s, n = map(int, parts)
    else:
        s = int(parts[0])
        n = int(input())

    dragons = []
    for _ in range(n):
        x, y = map(int, input().split())
        dragons.append((x, y))

    # Fight weakest first
    dragons.sort(key=lambda d: d[0])

    for x, y in dragons:
        if s > x:
            s += y
        else:
            print("NO")
            return

    print("YES")

if __name__ == "__main__":
    nextLvl()