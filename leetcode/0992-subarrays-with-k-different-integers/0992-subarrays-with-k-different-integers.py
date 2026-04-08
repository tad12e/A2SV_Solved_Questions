from collections import Counter
from typing import List

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def atMostK(k):
            count = 0
            freq = Counter()
            left = 0

            for right in range(len(nums)):
                if freq[nums[right]] == 0:
                    k -= 1  # a new distinct element
                freq[nums[right]] += 1

                while k < 0:  # too many distinct
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        k += 1
                    left += 1

                count += right - left + 1  # number of subarrays ending at right
            return count

        return atMostK(k) - atMostK(k - 1)

