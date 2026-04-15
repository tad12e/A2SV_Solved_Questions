from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq=Counter(nums)
        for i in nums:
            if freq[i]>=2:
                return i
                

        