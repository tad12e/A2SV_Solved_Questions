class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        di=defaultdict(int)

        for i in nums:
            di[i]+=1
        for key, value in di.items():
            if  value>=2:
                return True
        return False
        