from collections import Counter

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
    
        even_sum = sum(num for num in nums if num % 2 == 0)
        result = []

        for val, index in queries:
            original_value = nums[index]
        
            nums[index] += val
        
            if original_value % 2 == 0:  
                if nums[index] % 2 == 0:  
                    even_sum += val
                else:  
                    even_sum -= original_value
            else:  
                if nums[index] % 2 == 0:  
                    even_sum += nums[index]
            
            
            result.append(even_sum)

        return result

            
            