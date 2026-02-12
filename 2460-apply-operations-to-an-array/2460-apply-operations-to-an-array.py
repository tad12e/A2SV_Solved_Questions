class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        res=[0]*len(nums)

        for i in range(len(nums)-1):

            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        n=len(nums)-1
        m=0
        for i in nums:
            if i==0:
                res[n]=i
                n=n-1
            else:
                res[m]=i
                m=m+1
        return res




         
        