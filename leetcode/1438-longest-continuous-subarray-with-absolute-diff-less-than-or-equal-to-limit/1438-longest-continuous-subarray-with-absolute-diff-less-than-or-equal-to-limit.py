from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):

        maxDeque = deque()
        minDeque = deque()

        left = 0
        ans = 0

        for right in range(len(nums)):

            
            while maxDeque and nums[right] > maxDeque[-1]:
                maxDeque.pop()

            maxDeque.append(nums[right])

            
            while minDeque and nums[right] < minDeque[-1]:
                minDeque.pop()

            minDeque.append(nums[right])

            while maxDeque[0] - minDeque[0] > limit:

                if nums[left] == maxDeque[0]:
                    maxDeque.popleft()

                if nums[left] == minDeque[0]:
                    minDeque.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans