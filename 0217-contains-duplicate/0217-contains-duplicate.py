from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dect= Counter(nums)
        for i in nums:
            if dect[i]>=2:
                return True
        return False

        