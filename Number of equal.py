from collections import Counter

n, m=map(int, input().split())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
physical=set(arr1)
dect1=Counter(arr1)
dect2=Counter(arr2)

count=0

for i in physical:
    add=dect1[i]*dect2[i]
    count+=add

print(count)

