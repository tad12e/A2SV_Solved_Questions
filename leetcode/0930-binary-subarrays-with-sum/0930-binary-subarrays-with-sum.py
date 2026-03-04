from collections import Counter
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hashmap = {0: 1}
        total_sum = 0
        count = 0

        for num in nums:
            total_sum += num
            remainder = total_sum - goal
            if remainder in hashmap:
                count += hashmap[remainder]
            hashmap[total_sum] = hashmap.get(total_sum, 0) + 1

        return count


        