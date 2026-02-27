t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    if n == 2:
        print(2)
        print(*p)
        continue
    
    res = [p[0]]
    
    for i in range(1, n - 1):
        if (p[i] > p[i-1] and p[i] > p[i+1]) or \
           (p[i] < p[i-1] and p[i] < p[i+1]):
            res.append(p[i])
    
    res.append(p[-1])
    
    print(len(res))
    print(*res)
