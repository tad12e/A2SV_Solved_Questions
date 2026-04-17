from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mx=max(nums)
        freq=Counter(nums)
        if mx<0:
            return 1



        for i in range(1, mx+1):
            if freq[i]==0:
                return i
                
        else:
            return mx+1






        