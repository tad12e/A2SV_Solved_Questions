class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
       
        heaters.sort()
        glbl_max_radius = 0

        for house in houses:
           
            left = 0
            right = len(heaters) - 1
            
           
            while left <= right:
                mid = (left + right) // 2
                if heaters[mid] < house:
                    left = mid + 1
                else:
                    right = mid - 1
          
            
            dist_right = float('inf')
            dist_left = float('inf')
            
            if left < len(heaters):
                dist_right = heaters[left] - house
            
            if left > 0:
                dist_left = house - heaters[left - 1]
                
         
            current_house_radius = min(dist_left, dist_right)
           
            glbl_max_radius = max(glbl_max_radius, current_house_radius)
            
        return glbl_max_radius




        





        