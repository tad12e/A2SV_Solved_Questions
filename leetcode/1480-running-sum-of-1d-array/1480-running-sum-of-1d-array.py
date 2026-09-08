class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans=[]
        num=0
        
        for i in nums:
            num+=i
            ans.append(num)
        return ans

