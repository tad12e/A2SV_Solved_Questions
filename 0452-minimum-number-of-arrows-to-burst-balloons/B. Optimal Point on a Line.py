import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort()

# If n is odd -> middle element
# If n is even -> left median
print(arr[(n - 1) // 2])
