class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7

        prefix=[0]*len(nums)


        for i in requests:
            start, end=i

            prefix[start]+=1
            if end+1 < len(nums):
                prefix[end+1]-=1
        sm=0 
        arr=[]
        for i in prefix:
            sm+=i
            arr.append(sm)

        #print(arr)
        
        perms=[0]*len(nums)
        lis=[]
        for i in range(len(arr)):
            lis.append((i, arr[i]))
    





        nums.sort(reverse=True)
        sor=sorted(lis, reverse=True, key=lambda x:x[1])
        print(sor)
        print(arr)


        for i in range(len(nums)):
            perms[sor[i][0]]=nums[i]

        print(perms)


        pre=[]
        sm2=0
        ans=0


        for i in perms:
            sm2+=i
            pre.append(sm2)


        for start, end in requests:
            if start>0:
                ans+=pre[end]-pre[start-1]
            else:
                ans+=pre[end]

        print(pre)
        return ans%MOD

