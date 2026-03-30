class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans=0
        a, b=0,0
       
        j=0


        for i in range(len(nums)):
            if nums[i]==0:
                a+=1
            else:
                b+=1
            
            while a>1:
                if nums[j]==0:
                    a-=1
                else:
                    b-=1
                j+=1
            ans=max(ans, b)
        if a==0:
            return ans-1
        return ans

                
                
