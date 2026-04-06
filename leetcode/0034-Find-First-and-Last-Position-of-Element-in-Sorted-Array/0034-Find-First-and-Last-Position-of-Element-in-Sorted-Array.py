from collections import Counter
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        low=0
        high=len(nums)-1

        found=False
        res=[]
        freq=Counter(nums)


        for i in range(len(nums)):

            if nums[i]==target and found==False:
                res.append(i)
                freq[nums[i]]-=1
                found=True
            elif nums[i]==target and found==True:

                if freq[nums[i]]==1:
                    res.append(i)
                else:
                    freq[nums[i]]-=1

        if len(res)==0:
            return [-1,-1]
        if len(res)==1:
            h=res[0]
            return [h, h]


        return res