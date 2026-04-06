class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            # Calculate the middle index
            mid = (low + high) // 2
            
            # Check if the middle element is our target
            if nums[mid] == target:
                return mid
            
            # If target is greater, ignore the left half
            elif nums[mid] < target:
                low = mid + 1
            
            # If target is smaller, ignore the right half
            else:
                high = mid - 1
        
        # If we exit the loop, the target was not in the list
        return -1

            
        