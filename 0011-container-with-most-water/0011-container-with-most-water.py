class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1  # Start from both ends
        
        while left < right:
            current_height = min(height[left], height[right])
            current_width = right - left
            max_area = max(max_area, current_height * current_width)
            
            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area

        