class Solution:
    def findMin(self, nums: list[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If mid element is greater than the rightmost element,
            # the minimum must be in the right half
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                # Minimum is in left half (including mid)
                high = mid
        
        return nums[low]