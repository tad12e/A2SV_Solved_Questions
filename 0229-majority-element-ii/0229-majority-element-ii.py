from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        dect=Counter(nums)
        n=len(nums)
        res=[]

        for i in nums:
            if dect[i]>(n/3):
                if i not in res:
                    res.append(i)
        return res


        