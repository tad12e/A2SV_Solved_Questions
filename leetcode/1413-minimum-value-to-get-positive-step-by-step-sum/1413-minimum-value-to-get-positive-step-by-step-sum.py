class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        prefix=[]
        sm=0

        for i in nums:
            sm+=i
            prefix.append(sm)

        mn=min(prefix)
        if mn<0:
            return 0-mn+1
        else:
            return 1
        