from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[]
        dect=Counter(nums)

        for i in range(len(nums)):
            if dect[nums[i]]==2 and nums[i] not in res:
                res.append(nums[i])
        return res


        