n,s=map(int, input().split())

arr=list(map(int, input().split()))
ans=0
left=0
sm=0
found=False


for i in range(n):
    sm+=arr[i]
   
    
    while sm>=s:
        ans+=n-i
        
        sm-=arr[left]
        left+=1
    
print(ans)