class Solution:
    def minElement(self, nums: List[int]) -> int:
        arr=[]
        

        for i in range(len(nums)):
            sm=0
            for j in str(nums[i]):
                sm+=int(j)
            arr.append(sm)
        return min(arr)
