class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        arr=list(range(1, n+1))
        arr.append(n)
        nums.sort()

        if (n+1)!=len(nums):
            return False
        
        return nums==arr


