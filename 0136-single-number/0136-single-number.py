from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dect=Counter(nums)

        for i in nums:
            if dect[i]!=2:
                return i
        