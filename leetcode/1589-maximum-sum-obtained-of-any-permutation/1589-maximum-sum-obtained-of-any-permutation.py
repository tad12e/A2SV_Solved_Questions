class Solution:
    def maxSumRangeQuery(self, nums, requests):
        n = len(nums)
        freq = [0] * n

        # difference array
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end+1] -= 1

        # build actual frequency
        for i in range(1, n):
            freq[i] += freq[i-1]

        nums.sort()
        freq.sort()

        ans = 0
        MOD = 10**9 + 7
        
        for i in range(n):
            ans = (ans + nums[i] * freq[i]) % MOD

        return ans

