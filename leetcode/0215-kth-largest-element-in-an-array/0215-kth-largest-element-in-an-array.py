import random
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
      
        pivot = random.choice(nums)
        
       
        left  = [x for x in nums if x > pivot]  
        mid   = [x for x in nums if x == pivot] 
        right = [x for x in nums if x < pivot] 
        
        L, M = len(left), len(mid)
        
        if k <= L:
            
            return self.findKthLargest(left, k)
        elif k > (L + M):
            
            return self.findKthLargest(right, k - (L + M))
        else:
           
            return pivot
        