n, s = map(int, input().split())
arr = list(map(int, input().split()))
 
left = 0
sm = 0
ans = 0
 
for right in range(n):
    sm += arr[right]
 
    while sm > s:
        sm -= arr[left]
        left += 1
 
    ans += right - left + 1
 
print(ans)