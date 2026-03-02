class Solution:
    def countPartitions(self, nums: List[int]) -> int:

        sm=0
        total=sum(nums)
        ans=0


        for i in range(len(nums)):
            sm+=nums[i]
            curr_sum=total-sm

            if (sm-curr_sum)%2==0:
                ans+=1
        return ans-1 if ans>0 else ans

        