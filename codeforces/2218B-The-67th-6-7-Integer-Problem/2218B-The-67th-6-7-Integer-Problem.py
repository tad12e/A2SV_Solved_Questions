def solve():

    t=int(input())
    for _ in range(t):

        
        
        arr=list(map(int, input().split()))
        max_value=max(arr)
        ans=sum(arr)-(max_value)*2
        print(0-ans)
solve()