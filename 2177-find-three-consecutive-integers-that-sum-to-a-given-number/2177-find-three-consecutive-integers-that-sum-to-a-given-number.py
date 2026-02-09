class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        
        x = (num - 3) // 3
        
        
        if num < 3 and (num - 3) % 3 != 0:
           
            return [x, x + 1, x + 2]
        
        return [x, x + 1, x + 2] if (num - 3) % 3 == 0 else []
