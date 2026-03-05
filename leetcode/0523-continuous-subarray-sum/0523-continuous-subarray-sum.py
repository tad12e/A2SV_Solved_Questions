class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #Solution2 (Using HashMap and Math Fact)
        hashMap = dict()
        hashMap[0] = -1
        sum = 0
        for i,n in enumerate(nums):
            sum += n
            if sum % k in hashMap:
                length = i-hashMap[sum%k]
                if length >=2:
                    return True
            else:
                hashMap[sum%k]=i
        return False
        