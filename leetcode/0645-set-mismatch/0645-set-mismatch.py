from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        arr=list(range(1, len(nums)+1))
        ans=[]
        freq=Counter(nums)
        
        
        for i in nums:
            if freq[i]==2:
                ans.append(i)
                break
        for i in arr:

            if i not in nums:
                ans.append(i)
                break
        return ans
