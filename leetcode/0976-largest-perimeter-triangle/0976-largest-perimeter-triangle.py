class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)

        for i in range(2, len(nums)):
            a = nums[i-2]
            b = nums[i-1]
            c = nums[i]

            if a < b + c:
                return a + b + c

        return 0




        